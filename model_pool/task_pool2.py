import sys,os
sys.path.insert(0,os.path.abspath('.'))
sys.path.insert(0,os.path.abspath('..'))
sys.path.insert(0,os.path.abspath('../model_pool'))

import data_pre.module_parameters as pars
from abc import ABCMeta, abstractmethod
from model_pool.piplines import run_one_task
class BaseTask():
    __metaclass__ = ABCMeta
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def save(self):
        pass

class DataTask(BaseTask):
    def __init__(self,name):
        super(DataTask,self).__init__(name)
        self.data_par = pars.ParameterDict()
        self.data_par.load_JSON('../settings/base_data_settings.json')


    def save(self):
        self.data_par.write_ext_JSON('../settings/data_settings.json')

class ModelTask(BaseTask):
    def __init__(self,name):
        super(ModelTask,self).__init__(name)
        self.task_par = pars.ParameterDict()
        self.task_par.load_JSON('../settings/base_task_settings.json')

    def save(self):
        self.task_par.write_ext_JSON('../settings/task_settings.json')




# # ############## Task 1   input -1 1#############
# tsm = ModelTask('task_80')
# dm = DataTask('task_80')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='lpba'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# # tsm.task_par['tsk_set']['train'] = False
# # tsm.task_par['tsk_set']['dg_key_word'] = 'input1_s'
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 0
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/hist_th_0.06_lpba_seg_patchedmy_balanced_random_crop/task48_5_unetB_const_lr_100/checkpoints/epoch_100_"
# dm.data_par['datapro']['dataset']['task_name']='flicker_2_range_5'
# dm.data_par['datapro']['dataset']['prepare_data']=True
# dm.data_par['datapro']['seg']['save_train_custom']=False
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=True
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'task80_unet'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 100
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,2,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*100
#
#
# tsm.save()
# dm.save()
# run_one_task()
#




# # ############## Task 91   input -1 1#############
# tsm = ModelTask('task_91')
# dm = DataTask('task_91')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='lpba'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# # tsm.task_par['tsk_set']['train'] = False
# # tsm.task_par['tsk_set']['dg_key_word'] = 'input1_s'
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 0
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/hist_th_0.06_lpba_seg_patchedmy_balanced_random_crop/task48_5_unetB_const_lr_100/checkpoints/epoch_100_"
# dm.data_par['datapro']['dataset']['task_name']='axis_1_crop_shrink_no_flicker'
# dm.data_par['datapro']['dataset']['prepare_data']=True
# dm.data_par['datapro']['seg']['save_train_custom']=False
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[224,192,8]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[0,0,2]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'task81_unet'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 100
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,2,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8
#
#
# tsm.save()
# dm.save()
# run_one_task()


# ############## Task 91   input -1 1#############
# tsm = ModelTask('task_92')
# dm = DataTask('task_92')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='lpba'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# # tsm.task_par['tsk_set']['train'] = False
# # tsm.task_par['tsk_set']['dg_key_word'] = 'input1_s'
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 0
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/hist_th_0.06_lpba_seg_patchedmy_balanced_random_crop/task48_5_unetB_const_lr_100/checkpoints/epoch_100_"
# dm.data_par['datapro']['dataset']['task_name']='axis_1_crop_shrink_flicker_3'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['save_train_custom']=False
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=3
# dm.data_par['datapro']['seg']['patch_size']=[224,192,8]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[0,0,3]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=True
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=3
#
# tsm.task_par['tsk_set']['task_name'] = 'task92_unet'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 150
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,2,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*100
#
#
# tsm.save()
# dm.save()
# run_one_task()



# ############## Task 91   input -1 1#############
# tsm = ModelTask('task_93')
# dm = DataTask('task_93')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='lpba'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# # tsm.task_par['tsk_set']['train'] = False
# # tsm.task_par['tsk_set']['dg_key_word'] = 'input1_s'
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 0
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/hist_th_0.06_lpba_seg_patchedmy_balanced_random_crop/task48_5_unetB_const_lr_100/checkpoints/epoch_100_"
# dm.data_par['datapro']['dataset']['task_name']='axis_1_crop2_shrink_flicker_3'
# dm.data_par['datapro']['dataset']['prepare_data']=True
# dm.data_par['datapro']['seg']['save_train_custom']=False
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=3
# dm.data_par['datapro']['seg']['patch_size']=[112,96,32]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[18,15,8]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=True
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=3
#
# tsm.task_par['tsk_set']['task_name'] = 'task93_unet'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 150
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,2,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*100
#
#
# tsm.save()
# dm.save()
# run_one_task()




#
#
# # ############## Task 0   input -1 1#############
# tsm = ModelTask('task101')
# dm = DataTask('task_101')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =0
# tsm.task_par['tsk_set']['gpu_ids'] = 0
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_101_brast_unet/checkpoints/epoch_100_"
# dm.data_par['datapro']['dataset']['task_name']='brats_mbr'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_101_brast_unet'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 100
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,2,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8
#
#
# tsm.save()
# dm.save()
# run_one_task()
#





# # ############## Task 0   input -1 1#############
# tsm = ModelTask('task102')
# dm = DataTask('task_102')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# tsm.task_par['tsk_set']['save_fig_on'] = False
# # tsm.task_par['tsk_set']['train'] = False
# # tsm.task_par['tsk_set']['dg_key_word'] = 'input1_s'
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 0
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/hist_th_0.06_lpba_seg_patchedmy_balanced_random_crop/task48_5_unetB_const_lr_100/checkpoints/epoch_100_"
# dm.data_par['datapro']['dataset']['task_name']='brats_mbr'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_102_brast_unet_resid_only'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 200
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,2,1]# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8
#
#
# tsm.save()
# dm.save()
# run_one_task()
#







# # ############## Task 0   input -1 1#############
# tsm = ModelTask('task103d')
# dm = DataTask('task_103')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# # tsm.task_par['tsk_set']['train'] = False
# # tsm.task_par['tsk_set']['dg_key_word'] = 'input1_s'
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 2
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/hist_th_0.06_lpba_seg_patchedmy_balanced_random_crop/task48_5_unetB_const_lr_100/checkpoints/epoch_100_"
# dm.data_par['datapro']['dataset']['task_name']='brats_mbr'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_103_brast_unet_focal_lossresid_only'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 200
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8
#
#
# tsm.save()
# dm.save()
# run_one_task()



#
#
# ############## Task 0   input -1 1#############
# tsm = ModelTask('task105')
# dm = DataTask('task_105')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =0
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #0
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_brats_seg_patchedmy_balanced_random_crop/tsk_105_unet/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
# dm.data_par['datapro']['seg']['sched']='patched'
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_105_unet'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
#
#
# tsm.save()
# dm.save()
# run_one_task()
# #
# ############## Task 106   input -1 1#############
# tsm = ModelTask('task106')
# dm = DataTask('task_106')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 1  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_106_unet_resid_only'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
#
#
# tsm.save()
# dm.save()
# run_one_task()

#
#
# ############## Task 106   input -1 1#############
# tsm = ModelTask('task107')
# dm = DataTask('task_107')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =0
# tsm.task_par['tsk_set']['gpu_ids'] = 3  #0
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_brats_seg_patchedmy_balanced_random_crop/tsk_107_unet_focal_loss/checkpoints/epoch_250_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = '100 0.8'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
#
#
# tsm.save()
# dm.save()
# run_one_task()



#
#
# ############## Task 106   input -1 1#############
# tsm = ModelTask('task108')
# dm = DataTask('task_108')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_108_unet_focal_loss_resid'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
#
#
# tsm.save()
# dm.save()
# run_one_task()







#
# ############## Task 106   input -1 1#############
# tsm = ModelTask('task109')
# dm = DataTask('task_109')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 1  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_109_get_104_res'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
#
#
# tsm.save()
# dm.save()
# run_one_task()


#
#
# #
# # #
# # #
# # # #
#
# ############## Task 110   input -1 1#############
# tsm = ModelTask('task110')
# dm = DataTask('task_110')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids'] =3
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_brats_seg_patchedmy_balanced_random_crop/tsk_110_unet_resid_log1p5/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
# dm.data_par['datapro']['seg']['sched']='patched'
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_110_unet_resid_log1p5'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
#
#
# tsm.save()
# dm.save()
# run_one_task()

#
#
#
# ############## Task 106   input -1 1#############
# tsm = ModelTask('task111')
# dm = DataTask('task_111')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_111_unet_focal_loss_resid_log1p5'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 200
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 4   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()

# #
# ############## Task 106   input -1 1#############
# tsm = ModelTask('task111_1')
# dm = DataTask('task_111_1')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =0
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_brats_seg_patchedmy_balanced_random_crop/tsk_111_unet_focal_loss_resid_log1p5/checkpoints/epoch_200_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_111_1_unet_focal_loss_resid_log1p5'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 200
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 4   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
# #
# #
#
#


# ############## Task 112   input -1 1#############
# tsm = ModelTask('task112')
# dm = DataTask('task_112')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =0
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_112_unet_resid_ce_imd'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce_imd'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8   # the learning rate should be ajusted in brats cases
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()



#
# ############## Task 112   input -1 1#############
# tsm = ModelTask('task113')
# dm = DataTask('task_113')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_113_unet_resid_ce_imd_low_lr'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce_imd'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*2   # the learning rate should be ajusted in brats cases
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#
#



#
# ############## Task 112   input -1 1#############
# tsm = ModelTask('task200')
# dm = DataTask('task_200')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_200_unet1_3'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10   # the learning rate should be ajusted in brats cases
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#








# ############## Task 112   input -1 1#############
# tsm = ModelTask('task201')
# dm = DataTask('task_201')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_brats_seg_patchedmy_balanced_random_crop/tsk_201_unet1_3_all_on/checkpoints/epoch_250_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_201_unet1_3_all_on'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =2
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10   # the learning rate should be ajusted in brats cases
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()




#
# ############## Task 112   input -1 1#############
# tsm = ModelTask('task202')
# dm = DataTask('task_202')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_brats_seg_patchedmy_balanced_random_crop/tsk_202_unet1_3_all_on/checkpoints/epoch_250_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = ' '  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =20
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10   # the learning rate should be ajusted in brats cases
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#


#
# ############## Task 112   input -1 1#############
# tsm = ModelTask('task220')
# dm = DataTask('task_220')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='lpba'
# dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='hist_th_0.06'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_220_unet1_4'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =20
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10   # the learning rate should be ajusted in brats cases
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#





#
#
# ############## Task 112   input -1 1#############
# tsm = ModelTask('task230')
# dm = DataTask('task_230')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='lpba'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 3  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='hist_th_0.06'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_230_unet1_3'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =20
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10   # the learning rate should be ajusted in brats cases
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#
#
#



#
# ############## Task 112   input -1 1#############
# tsm = ModelTask('task210')
# dm = DataTask('task_210')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# # dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_95_brats_seg_patchedmy_balanced_random_crop/tsk_210_unet1_4_all_on/checkpoints/epoch_200_"
# dm.data_par['datapro']['dataset']['task_name']='brats_95'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.05
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_210_unet1_4_all_on'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 200
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =20
# tsm.task_par['tsk_set']['loss']['update_epoch'] =2   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8   # the learning rate should be ajusted in brats cases
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()


#
# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_221')
# dm = DataTask('task_221')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =0
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_brats_seg_patchedmy_balanced_random_crop/tsk221_t9_base/checkpoints/epoch_500_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='patched'
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk221_t9_base'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3Dt9'
# tsm.task_par['tsk_set']['epoch'] = 500
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()


#
#
# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_221')
# dm = DataTask('task_221')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids'] =0
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_brats_seg_nopatchedmy_balanced_random_crop/tsk221_t9_base/checkpoints/model_best.pth.tar"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk221_t9_base'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3Dt9'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#
#
# #
# #
# #
# #
#
#
#
# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_221')
# dm = DataTask('task_221')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_freecrop_brats_seg_nopatchedmy_balanced_random_crop/tsk221_t9_base/checkpoints/model_best.pth.tar"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_freecrop'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.0
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk221_t9_base'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3Dt9'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lrllm'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()

#
#
#
#
# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_221')
# dm = DataTask('task_221')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 3  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_freecrop_brats_seg_nopatchedmy_balanced_random_crop/tsk221_t9_sim/checkpoints/model_best.pth.tar"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_freecrop'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.0
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk221_t9_sim'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3Dt9_sim'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#







#
#
# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_221')
# dm = DataTask('task_221')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_freecrop_brats_seg_nopatchedmy_balanced_random_crop/tsk221_UNet3DB/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_freecrop'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.0
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk221_UNet3DB'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()







#
#
#
# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_221')
# dm = DataTask('task_221')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids'] =0
# tsm.task_par['tsk_set']['gpu_ids'] = 3  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_freecrop_brats_seg_nopatchedmy_balanced_random_crop/tsk221_t9_sim_const_lr/checkpoints/model_best.pth.tar"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_freecrop'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.0
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk221_t9_sim_const_lr'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3Dt9_sim'
# tsm.task_par['tsk_set']['epoch'] = 400
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.9   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#
#
#
#
# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_221')
# dm = DataTask('task_221')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids'] =3
# tsm.task_par['tsk_set']['gpu_ids'] = 3  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_freecrop_brats_seg_nopatchedmy_balanced_random_crop/tsk221_t9_sim_channel3/checkpoints/model_best.pth.tar"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_freecrop'
# dm.data_par['datapro']['dataset']['prepare_data'] =False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.0
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk221_t9_sim_channel3'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3Dt9_sim'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#
#


#
#
#
#
#
# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_222')
# dm = DataTask('task_222')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_brats_seg_patchedmy_balanced_random_crop/tsk222_t8_base/checkpoints/epoch_250_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk222_t8_base'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3Dt8'
#
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()

#
#
#
#


#
#
# ############## Task 112   input -1 1#############
# tsm = ModelTask('task_223')
# dm = DataTask('task_223')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='lpba'
# dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =3
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] =''# "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='hist_th_0.06'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']= 5
#
# tsm.task_par['tsk_set']['task_name'] = 'task223_vonet_light1'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'vonet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =4
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['voting']['start_saving_model'] = 50
# tsm.task_par['tsk_set']['voting']['saving_voting_per_epoch'] = 1
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,2,1]
# tsm.task_par['tsk_set']['save_val_fig_epoch'] =4
#
#
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8   # the learning rate should be ajusted in brats cases
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()






#
# tsm = ModelTask('task_224')
# dm = DataTask('task_224')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =0
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = ''#"/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']= 5
#
# tsm.task_par['tsk_set']['task_name'] = 'task224_vonet_light1'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'vonet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =4
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1   ###### pay attention guy################
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 5
#
# tsm.task_par['tsk_set']['voting']['start_saving_model'] = 50
# tsm.task_par['tsk_set']['voting']['saving_voting_per_epoch'] = 1
# tsm.task_par['tsk_set']['voting']['voting_save_sched'] = 'default'
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,2,1]
# tsm.task_par['tsk_set']['save_val_fig_epoch'] =4
#
#
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8   # the learning rate should be ajusted in brats cases
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#
#







#
# tsm = ModelTask('task_225')
# dm = DataTask('task_225')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 1  #1
#
# tsm.task_par['tsk_set']['model_path'] ="" # "/playpen/zyshen/data/brats_mbr_brats_seg_patchedmy_balanced_random_crop/tsk_104_brast_unet_focal_loss/checkpoints/epoch_150_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
# dm.data_par['datapro']['seg']['sched']='patched'
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']= 5
#
# tsm.task_par['tsk_set']['task_name'] = 'task225_comp224_ce_imd'  #task42_unet4_base
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'vonet'
# tsm.task_par['tsk_set']['network_name'] ='UNet_asm'
#
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =4
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1   ###### pay attention guy################
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= True
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce_imd'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 20
#
# tsm.task_par['tsk_set']['voting']['start_saving_model'] = 100
# tsm.task_par['tsk_set']['voting']['saving_voting_per_epoch'] = 1
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2   #  batch update every crtitcUpdates
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,2,1]
# tsm.task_par['tsk_set']['save_val_fig_epoch'] =4
#
#
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*8   # the learning rate should be ajusted in brats cases
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.1   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
# #

#
#
#
# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_230')
# dm = DataTask('task_230')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =0
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_freecrop_brats_seg_nopatchedmy_balanced_random_crop/tsk221_t9_sim_const_lr/epoch_250_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_freecrop'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.0
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk230_UNet3D_Deep'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3D_Deep'
# tsm.task_par['tsk_set']['epoch'] = 400
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 4
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 1
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*1
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()










# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_240')
# dm = DataTask('task_240')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/raid/zyshen/data/brats_com_freecrop_brats_seg_nopatchedmy_balanced_random_crop/tsk240_UNet3DMM/checkpoints/model_best.pth.tar"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_freecrop'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.0
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk240_UNet3DMM'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DMM'
# tsm.task_par['tsk_set']['epoch'] = 300
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,1]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*1
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()








# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_251')
# dm = DataTask('task_251')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =0
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk251_UNet3D_Deep/checkpoints/epoch_260_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk251_UNet3D_Deep' # already renamed as tsl251_t9_sim #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3Dt9_sim'
# tsm.task_par['tsk_set']['epoch'] = 400
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*5
# #tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.5   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#








# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_251')
# dm = DataTask('task_251')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk251_t9_loc/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk251_t9_loc'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3Dt9_sim'
# tsm.task_par['tsk_set']['epoch'] = 300
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*5
# #tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.5   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()


# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_251')
# dm = DataTask('task_251')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk251_unet_loc_f/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk251_unet_loc_f'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 300
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*5
# #tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.5   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#




#
#
# # # ############## Task 0   input -1 1#############
# tsm = ModelTask('task_251')
# dm = DataTask('task_251')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =1
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/raid/zyshen/data/brats_com_freecrop_brats_seg_nopatchedmy_balanced_random_crop/tsk240_UNet3DMM/checkpoints/model_best.pth.tar"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk251_UNet3DMM'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DMM'
# tsm.task_par['tsk_set']['epoch'] = 300
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*5
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#
#
#






#
#
# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_251')
# dm = DataTask('task_251')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids']=1
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk251_unet_loc_f/checkpoints/epoch_130_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk251_unet_loc_f_test'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 300
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*5
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()





#
#
# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_261')
# dm = DataTask('task_261')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids']=0
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk261_unet_base/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk261_unet_base'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#





#
#
#
#
#
#
# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_261_1')
# dm = DataTask('task_261_1')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids']=0
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk261_1_unet_loc/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk261_1_unet_loc'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB_loc'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#
#
#
#
#
#
#













# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_261_new_ce_custom')
# dm = DataTask('task_261_new_ce_custom')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids']=1
# tsm.task_par['tsk_set']['gpu_ids'] = 0   #1  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/task_261_new_ce_custom/checkpoints/epoch_240_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=-1
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'task_261_new_ce_custom'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 360
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()





# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_261_new_wce_custom')
# dm = DataTask('task_261_new_wce_custom')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids']=1
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk261_new_unet_wce_custom/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=-1
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk261_new_unet_wce_custom'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 300
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =5
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 10
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()




# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_261_new_wce_rand')
# dm = DataTask('task_261_new_wce_rand')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids']=3
# tsm.task_par['tsk_set']['gpu_ids'] = 3  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk261_new_unet_wce_rand/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=-1
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk261_new_unet_wce_rand'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =5
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 10
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#



# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_261_new_wce_bg_avg_custom')
# dm = DataTask('task_261_new_wce_bg_avg_custom')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids']=0
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
# 
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/task_261_new_wce_bg_avg_custom/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
# 
# 
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=-1
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
# 
# 
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
# 
# tsm.task_par['tsk_set']['task_name'] = 'task_261_new_wce_bg_avg_custom'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =5
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
# 
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['only_bg_avg_update'] = True
# tsm.task_par['tsk_set']['loss']['only_bg_avg_log_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 10
# 
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
# 
# 
# tsm.save()
# dm.save()
# run_one_task()





#
# #
# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_261_new_wce_bg_log_avg_custom')
# dm = DataTask('task_261_new_wce_bg_log_avg_custom')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids']=0
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# #tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk261_1_unet_loc/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=-1
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'task_261_new_wce_bg_log_avg_custom'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =5
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['only_bg_avg_update'] = False
# tsm.task_par['tsk_set']['loss']['only_bg_avg_log_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 10
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()




# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_261_new_fl_custom')
# dm = DataTask('task_261_new_fl_custom')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids']=2
# tsm.task_par['tsk_set']['gpu_ids'] = 2  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/task_261_new_fl_custom/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=-1
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'task_261_new_fl_custom'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()




#
# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_261_new_ce_custom_test')
# dm = DataTask('task_261_new_ce_custom_test')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids']=0
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/raid/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/task_261_new_ce_custom/checkpoints/epoch_160_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=-1
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'task_261_new_ce_custom_test'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()






################ Task 0   input -1 1#############
# tsm = ModelTask('task_261_datanew')
# dm = DataTask('task_261_datanew')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids']=0
# tsm.task_par['tsk_set']['gpu_ids'] = 1  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk261_1_unet_loc/checkpoints/epoch_last_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_full_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=-1
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk261_datanew_unet_base'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#










#
# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_262')
# dm = DataTask('task_262')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids']=1
# tsm.task_par['tsk_set']['gpu_ids'] = 1  #1
#
# tsm.task_par['tsk_set']['model_path'] = ""#""/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk262_vnet_unet_base/checkpoints/epoch_200_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk262_vnet_unet_base'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet_asm_f'
# tsm.task_par['tsk_set']['epoch'] = 300
# tsm.task_par['tsk_set']['model'] = 'vonet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
#
# tsm.task_par['tsk_set']['loss']['update_epoch'] =10  #################
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 200
#
# tsm.task_par['tsk_set']['voting']['start_saving_model'] = 200
# tsm.task_par['tsk_set']['voting']['saving_voting_per_epoch'] = 10
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()




#
#
# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_263')
# dm = DataTask('task_263')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids']=1
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk251_unet_loc_f/checkpoints/epoch_130_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk263_focal_loss_weighted'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 250
# tsm.task_par['tsk_set']['model'] = 'unet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
#
# tsm.task_par['tsk_set']['loss']['update_epoch'] =10  #################
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = True   # from task263 this provide more smooth version of only_resid
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 20
#
# tsm.task_par['tsk_set']['voting']['start_saving_model'] = 200
# tsm.task_par['tsk_set']['voting']['saving_voting_per_epoch'] = 10
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()



#
# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_264')
# dm = DataTask('task_264')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =True
# tsm.task_par['tsk_set']['old_gpu_ids']=1
# tsm.task_par['tsk_set']['gpu_ids'] = 3  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk264_vnet_t9_base/checkpoints/epoch_200_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk264_vnet_t9_base'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet_asm_t9'
# tsm.task_par['tsk_set']['epoch'] = 300
# tsm.task_par['tsk_set']['model'] = 'vonet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
#
# tsm.task_par['tsk_set']['loss']['update_epoch'] =10  #################
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 201
#
# tsm.task_par['tsk_set']['voting']['start_saving_model'] = 200
# tsm.task_par['tsk_set']['voting']['saving_voting_per_epoch'] = 10
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()
#
#
#






# ################ Task 0   input -1 1#############
# tsm = ModelTask('task_265')
# dm = DataTask('task_265')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# # tsm.task_par['tsk_set']['save_fig_on'] = False
# tsm.task_par['tsk_set']['train'] = True
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids']=1
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk251_unet_loc_f/checkpoints/epoch_130_"
# dm.data_par['datapro']['dataset']['task_name']='brats_com_ff_th01'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['sched']='nopatched'
#
#
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
# dm.data_par['datapro']['seg']['save_train_custom']=True
# dm.data_par['datapro']['seg']['num_flicker_per_train_img']=2
# dm.data_par['datapro']['seg']['patch_size']=[72,72,72]
# dm.data_par['datapro']['seg']['partition']['overlap_size']=[16,16,16]
# dm.data_par['datapro']['seg']['partition']['flicker_on']=False
# dm.data_par['datapro']['seg']['partition']['flicker_mode']='rand'
# dm.data_par['datapro']['seg']['partition']['flicker_range']=5
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk265_vnet_t9_con'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet_asm_t9_con'
# tsm.task_par['tsk_set']['epoch'] = 300
# tsm.task_par['tsk_set']['model'] = 'vonet'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
#
# tsm.task_par['tsk_set']['loss']['update_epoch'] =10  #################
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'ce'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = True
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = True
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = True
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 200
#
# tsm.task_par['tsk_set']['voting']['start_saving_model'] = 200
# tsm.task_par['tsk_set']['voting']['saving_voting_per_epoch'] = 10
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*10
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.8   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()






# #
# #
# #
# #
# ############## Task 0   input -1 1#############
#
# tsm = ModelTask('task_0')
# dm = DataTask('task_0')
# dm.data_par['datapro']['task_type']='seg'
# dm.data_par['datapro']['dataset']['dataset_name']='brats'
# #dm.data_par['datapro']['dataset']['output_path']='/playpen/raid/zyshen/data/'
# tsm.task_par['tsk_set']['train'] = False
# tsm.task_par['tsk_set']['dg_key_word'] = ''
# tsm.task_par['tsk_set']['save_by_standard_label'] = True
# tsm.task_par['tsk_set']['continue_train'] =False
# tsm.task_par['tsk_set']['old_gpu_ids'] =2
# tsm.task_par['tsk_set']['gpu_ids'] = 0  #1
#
# tsm.task_par['tsk_set']['model_path'] = ""# "/playpen/zyshen/data/brats_com_ff_th01_brats_seg_nopatchedmy_balanced_random_crop/tsk251_t9_loc/checkpoints/epoch_100_"
# tsm.task_par['tsk_set']['model_folder_path'] = "/playpen/zyshen/data/brats_com_brats_seg_patchedmy_balanced_random_crop/tsk_110_unet_resid_log1p5/checkpoints"
# tsm.task_par['tsk_set']['model_epoch_list'] = list(range(100,250,20))
# dm.data_par['datapro']['dataset']['task_name']='debug0'
# dm.data_par['datapro']['dataset']['prepare_data']=False
# dm.data_par['datapro']['seg']['num_crop_per_class_per_train_img']=30
# dm.data_par['datapro']['seg']['transform']['transform_seq']=['my_balanced_random_crop']
# dm.data_par['datapro']['seg']['transform']['my_bal_rand_crop']['scale_ratio']= 0.1
#
#
#
# tsm.task_par['tsk_set']['task_name'] = 'tsk_1'  #task42_unet4_base
# tsm.task_par['tsk_set']['network_name'] ='UNet3DB'
# tsm.task_par['tsk_set']['epoch'] = 300
# tsm.task_par['tsk_set']['model'] = 'asm_net_test'
# tsm.task_par['tsk_set']['batch_sz'] = 2
# tsm.task_par['tsk_set']['val_period'] =10
# tsm.task_par['tsk_set']['loss']['update_epoch'] =-1
# tsm.task_par['tsk_set']['loss']['imd_weighted_loss_on']= False
#
# tsm.task_par['tsk_set']['loss']['type'] = 'focal_loss'
# tsm.task_par['tsk_set']['loss']['ce']['weighted'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['log_update'] = False
# tsm.task_par['tsk_set']['loss']['only_resid_update'] = False
# tsm.task_par['tsk_set']['loss']['density_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['continuous_update'] = False
# tsm.task_par['tsk_set']['loss']['residue_weight_momentum'] = 0.1
# tsm.task_par['tsk_set']['loss']['focal_loss_weight_on'] = False
# tsm.task_par['tsk_set']['loss']['activate_epoch'] = 0
#
# tsm.task_par['tsk_set']['criticUpdates'] = 2
# tsm.task_par['tsk_set']['max_batch_num_per_epoch'] = [400,4,4]
# tsm.task_par['tsk_set']['optim']['lr'] = 0.001/2
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['type'] = 'custom'
# tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['step_size'] = 4000*5
# #tsm.task_par['tsk_set']['optim']['lr_scheduler']['custom']['gamma'] = 0.5   # the learning rate should be ajusted in brats cases
#
#
# tsm.save()
# dm.save()
# run_one_task()