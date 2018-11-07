import os
import numpy as np
import time
import SimpleITK as sitk
import subprocess
from model_pool.nifty_reg_utils import expand_batch_ch_dim, nifty_reg_affine, nifty_reg_resample

from model_pool.utils import factor_tuple
from model_pool.global_variable import *

def smooth_and_resample(image, shrink_factor, smoothing_sigma):
    """
    Args:
        image: The image we want to resample.
        shrink_factor: A number greater than one, such that the new image's size is original_size/shrink_factor.
        smoothing_sigma: Sigma for Gaussian smoothing, this is in physical (image spacing) units, not pixels.
    Return:
        Image which is a result of smoothing the input and then resampling it using the given sigma and shrink factor.
    """
    smoothed_image = sitk.SmoothingRecursiveGaussian(image, smoothing_sigma)

    original_spacing = image.GetSpacing()
    original_size = image.GetSize()
    new_size = [int(sz / float(shrink_factor) + 0.5) for sz in original_size]
    new_spacing = [((original_sz - 1) * original_spc) / (new_sz - 1)
                   for original_sz, original_spc, new_sz in zip(original_size, original_spacing, new_size)]
    return sitk.Resample(smoothed_image, new_size, sitk.Transform(),
                         sitk.sitkLinear, image.GetOrigin(),
                         new_spacing, image.GetDirection(), 0.0,
                         image.GetPixelID())


def get_affined_moving_image(fixed_image_pth, moving_image_path,ml_path=None):
    affine_path =moving_image_path.replace('moving.nii.gz','affine.nii.gz')
    affine_txt = moving_image_path.replace('moving.nii.gz', 'affine_transform.txt')
    cmd = nifty_reg_affine(ref=fixed_image_pth, flo=moving_image_path, aff=affine_txt, res=affine_path)
    affine_label_path = None

    if ml_path is not None:
        affine_label_path =moving_image_path.replace('moving.nii.gz', 'warped_label.nii.gz')
        cmd += '\n' + nifty_reg_resample(ref=fixed_image_pth,flo=ml_path,trans=affine_txt, res=affine_label_path, inter= 0)
    process = subprocess.Popen(cmd, shell=True)
    process.wait()

    affine_image_cp = sitk.ReadImage(affine_path)
    affine_image_array = sitk.GetArrayFromImage(affine_image_cp)
    affine_image_array[np.isnan(affine_image_array)] = 0.
    affine_image = sitk.GetImageFromArray(affine_image_array)
    affine_image.SetSpacing(affine_image_cp.GetSpacing())
    affine_image.SetOrigin(affine_image_cp.GetOrigin())
    affine_image.SetDirection(affine_image_cp.GetDirection())
    sitk.WriteImage(affine_image, affine_path)


    return affine_path, affine_label_path





def multiscale_demons(registration_algorithm,
                      fixed_image_pth, moving_image_pth, initial_transform=None,
                      shrink_factors=None, smoothing_sigmas=None):
    """
    Run the given registration algorithm in a multiscale fashion. The original scale should not be given as input as the
    original images are implicitly incorporated as the base of the pyramid.
    Args:
        registration_algorithm: Any registration algorithm that has an Execute(fixed_image, moving_image, displacement_field_image)
                                method.
        fixed_image: Resulting transformation maps points from this image's spatial domain to the moving image spatial domain.
        moving_image: Resulting transformation maps points from the fixed_image's spatial domain to this image's spatial domain.
        initial_transform: Any SimpleITK transform, used to initialize the displacement field.
        shrink_factors: Shrink factors relative to the original image's size.
        smoothing_sigmas: Amount of smoothing which is done prior to resmapling the image using the given shrink factor. These
                          are in physical (image spacing) units.
    Returns:
        SimpleITK.DisplacementFieldTransform
    """
    # Create image pyramid.
    fixed_image = sitk.ReadImage(fixed_image_pth)
    moving_image = sitk.ReadImage(moving_image_pth)

    fixed_images = [fixed_image]
    moving_images = [moving_image]
    if shrink_factors:
        for shrink_factor, smoothing_sigma in reversed(list(zip(shrink_factors, smoothing_sigmas))):
            fixed_images.append(smooth_and_resample(fixed_images[0], shrink_factor, smoothing_sigma))
            moving_images.append(smooth_and_resample(moving_images[0], shrink_factor, smoothing_sigma))

    # Create initial displacement field at lowest resolution.
    # Currently, the pixel type is required to be sitkVectorFloat64 because of a constraint imposed by the Demons filters.
    if initial_transform:
        initial_displacement_field = sitk.TransformToDisplacementField(initial_transform,
                                                                       sitk.sitkVectorFloat64,
                                                                       fixed_images[-1].GetSize(),
                                                                       fixed_images[-1].GetOrigin(),
                                                                       fixed_images[-1].GetSpacing(),
                                                                       fixed_images[-1].GetDirection())
    else:
        initial_displacement_field = sitk.Image(fixed_images[-1].GetWidth(),
                                                fixed_images[-1].GetHeight(),
                                                fixed_images[-1].GetDepth(),
                                                sitk.sitkVectorFloat64)
        initial_displacement_field.CopyInformation(fixed_images[-1])

    # Run the registration.
    initial_displacement_field = registration_algorithm.Execute(fixed_images[-1],
                                                                moving_images[-1],
                                                                initial_displacement_field)
    # Start at the top of the pyramid and work our way down.
    for f_image, m_image in reversed(list(zip(fixed_images[0:-1], moving_images[0:-1]))):
        initial_displacement_field = sitk.Resample(initial_displacement_field, f_image)
        initial_displacement_field = registration_algorithm.Execute(f_image, m_image, initial_displacement_field)
    return sitk.DisplacementFieldTransform(initial_displacement_field)



def sitk_grid_sampling(fixed,moving, displacement,is_label=False):
    resampler = sitk.ResampleImageFilter()
    resampler.SetReferenceImage(fixed)
    interpolator = sitk.sitkNearestNeighbor if is_label else sitk.sitkLinear
    resampler.SetInterpolator(interpolator)
    resampler.SetDefaultPixelValue(0)
    resampler.SetTransform(displacement)
    out = resampler.Execute(moving)
    return out


def performDemonsRegistration(mv_path, target_path, registration_type='demons', record_path = None, ml_path=None,tl_path= None):

    start = time.time()

    print("start demons registration")
    assert registration_type =='demons'

    mv_path, ml_path = get_affined_moving_image(target_path, mv_path, ml_path=ml_path)


    demons_filter = sitk.FastSymmetricForcesDemonsRegistrationFilter()
    demons_filter.SetNumberOfIterations(30)
    # Regularization (update field - viscous, total field - elastic).
    demons_filter.SetSmoothDisplacementField(True)
    demons_filter.SetStandardDeviations(0.5)  #1,4

    # Run the registration.
    print("!!!!!!!!!!demons param{}".format(param_in_demons) )
    tx = multiscale_demons(registration_algorithm=demons_filter,
                           fixed_image_pth=target_path,
                           moving_image_pth=mv_path,
                           shrink_factors=None,#[4, 2],
                           smoothing_sigmas=param_in_demons) #[2,1],[4, 2]) (8,4)
    warped_img = sitk_grid_sampling(sitk.ReadImage(target_path), sitk.ReadImage(mv_path), tx,
                                    is_label=False)
    warped_label = sitk_grid_sampling(sitk.ReadImage(tl_path), sitk.ReadImage(ml_path), tx,
                                      is_label=True)

    print('demons registration finished and takes: :', time.time() - start)


    output  = sitk.GetArrayFromImage(warped_img)
    loutput = sitk.GetArrayFromImage(warped_label)
    # phi = sitk.GetArrayFromImage(tx.GetDisplacementField())
    # """ todo  check that whether the xyz order is the same as the interpolation assumed"""
    # phi = np.transpose(phi,(3,0,1,2))


    return expand_batch_ch_dim(output), expand_batch_ch_dim(loutput), None #np.expand_dims(phi,0)