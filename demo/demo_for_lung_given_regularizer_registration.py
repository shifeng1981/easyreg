import matplotlib as matplt
matplt.use('Agg')

import sys,os
sys.path.insert(0,os.path.abspath('.'))
sys.path.insert(0,os.path.abspath('..'))
sys.path.insert(0,os.path.abspath('../model_pool'))
sys.path.insert(0,os.path.abspath('../mermaid'))
from model_pool.global_variable import *
import data_pre.module_parameters as pars
from abc import ABCMeta, abstractmethod
from model_pool.piplines import run_one_task
from data_pre.reg_data_utils import write_list_into_txt, get_file_name
import numpy as np

class BaseTask():
    __metaclass__ = ABCMeta
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def save(self):
        pass

class DataTask(BaseTask):
    """
    load the data settings from json
    """
    def __init__(self,name,path='../settings/base_data_settings.json'):
        super(DataTask,self).__init__(name)
        self.data_par = pars.ParameterDict()
        self.data_par.load_JSON(path)


    def save(self, path='../settings/data_settings.json'):
        self.data_par.write_ext_JSON(path)

class ModelTask(BaseTask):
    """
    load the task settings from json
    """
    def __init__(self,name,path='../settings/base_task_settings.json'):
        super(ModelTask,self).__init__(name)
        self.task_par = pars.ParameterDict()
        self.task_par.load_JSON(path)

    def save(self,path= '../settings/task_settings.json'):
        self.task_par.write_ext_JSON(path)



def force_setting(dm, tsm,output_path):
    task_full_path = os.path.join(os.path.join(output_path,'reg'),'res')
    dm.data_par['datapro']['dataset']['prepare_data'] = False
    dm.data_par['datapro']['reg']['max_pair_for_loading'] = [1, 1, -1, 1]
    tsm.task_par['tsk_set']['train'] = False
    tsm.task_par['tsk_set']['save_by_standard_label'] = True
    tsm.task_par['tsk_set']['continue_train'] = False
    tsm.task_par['tsk_set']['reg']['mermaid_net']['using_sym'] = False
    data_json_path = os.path.join(task_full_path, 'cur_data_setting.json')
    tsk_json_path = os.path.join(task_full_path, 'cur_task_setting.json')
    tsm.save(tsk_json_path)
    dm.save(data_json_path)
    tsm.save()
    dm.save()


def init_env(task_full_path,output_path, source_path_list, target_path_list, l_source_path_list=None, l_target_path_list=None):
    """
    :param task_full_path:  the path of a completed task
    :param source_path: path of the source image
    :param target_path: path of the target image
    :param l_source: path of the label of the source image
    :param l_target: path of the label of the target image
    :return: None
    """
    dm_json_path = os.path.join(task_full_path, 'cur_data_setting.json')
    tsm_json_path = os.path.join(task_full_path, 'cur_task_setting.json')
    dm = DataTask('task_reg',dm_json_path)
    tsm = ModelTask('task_reg',tsm_json_path)
    file_num = len(source_path_list)
    assert len(source_path_list) == len(target_path_list)
    if l_source_path_list is not None and l_target_path_list is not None:
        assert len(source_path_list) == len(l_source_path_list)
        file_list = [[source_path_list[i], target_path_list[i],l_source_path_list[i],l_target_path_list[i]] for i in range(file_num)]
    else:
        file_list = [[source_path_list[i], target_path_list[i]] for i in range(file_num)]
    os.makedirs(os.path.join(output_path,'reg/test'),exist_ok=True)
    os.makedirs(os.path.join(output_path,'reg/res'),exist_ok=True)
    pair_txt_path =  os.path.join(output_path,'reg/test/pair_path_list.txt')
    fn_txt_path =   os.path.join(output_path,'reg/test/pair_name_list.txt')
    fname_list = [get_file_name(file_list[i][0])+'_'+get_file_name(file_list[i][1]) for i in range(file_num)]
    write_list_into_txt(pair_txt_path,file_list)
    write_list_into_txt(fn_txt_path,fname_list)
    root_path = output_path
    data_task_name = 'reg'
    cur_task_name = 'res'
    dm.data_par['datapro']['dataset']['output_path'] = root_path
    dm.data_par['datapro']['dataset']['task_name'] = data_task_name
    tsm.task_par['tsk_set']['task_name'] = cur_task_name
    return dm, tsm

def loading_img_list_from_files(path):
    from data_pre.reg_data_utils import read_txt_into_list
    path_list = read_txt_into_list(path)
    num_pair = len(path_list)
    assert len(path_list[0])>=2
    has_label = True if len(path_list[0])==4 else False
    source_path_list = [path_list[i][0] for i in range(num_pair)]
    target_path_list = [path_list[i][1] for i in range(num_pair)]
    l_source_path_list = None
    l_target_path_list = None
    if has_label:
        l_source_path_list = [path_list[i][2] for i in range(num_pair)]
        l_target_path_list = [path_list[i][3] for i in range(num_pair)]
    return source_path_list, target_path_list, l_source_path_list, l_target_path_list










read_img_list_from_txt=False
img_list_txt_path = '/playpen/zyshen/debugs/get_val_and_debug_res/test.txt'#'/playpen/zyshen/data/reg_debug_labeled_oai_reg_inter/test/pair_path_list.txt'
if not read_img_list_from_txt:
    source_path_list = ['/playpen/zyshen/debugs/9002116_20060804_SAG_3D_DESS_RIGHT_11269909_image.nii.gz']
    target_path_list = ['/playpen/zyshen/debugs/9002116_20050715_SAG_3D_DESS_RIGHT_10423916_image.nii.gz']
    l_source_path_list = [
        '/playpen/zyshen/debugs/9002116_20060804_SAG_3D_DESS_RIGHT_11269909_prediction_step1_batch6_16_reflect.nii.gz']
    l_target_path_list = [
        '/playpen/zyshen/debugs/9002116_20050715_SAG_3D_DESS_RIGHT_10423916_prediction_step1_batch6_16_reflect.nii.gz']
else:
    source_path_list, target_path_list,l_source_path_list,l_target_path_list = loading_img_list_from_files(img_list_txt_path)


task_full_path = '/playpen/zyshen/data/reg_debug_labeled_oai_reg_inter/test_intra_mermaid_net_500thisinst_10reg_double_loss_step3_jacobi'

    #'/playpen/zyshen/data/reg_debug_3000_pair_oai_reg_intra/vm_miccal_setting_zeroboundary_withbothlambda100sigma002withenlargedflowreg'
    #'/playpen/zyshen/data/reg_debug_labeled_oai_reg_inter/test_intra_mermaid_net_500thisinst_10reg_double_loss_step3_jacobi'
""" the path of the setting from a completed task"""

output_path = '/playpen/zyshen/debugs/todel_'
dm, tsm = init_env(task_full_path,output_path,source_path_list,target_path_list,l_source_path_list,l_target_path_list)
optional_setting_on = True
tsm.task_par['tsk_set']['gpu_ids'] = 3


if optional_setting_on:
    """ the following settings are optional, if you want do something different than the loaded setting"""
    ############################### general settings ##########################

    tsm.task_par['tsk_set']['network_name'] ='svf'
    tsm.task_par['tsk_set']['model'] = 'mermaid_iter'
    tsm.task_par['tsk_set']['batch_sz'] = 4  # multi sample registration is only for mermaid based methods, for other methods should always be 1
    tsm.task_par['tsk_set']['model_path'] = ''
#############################  for mermaid optimization registration ######################################3
    tsm.task_par['tsk_set']['reg']['mermaid_iter']={}
    """ settings for the mermaid optimization version, we only provide parameter that may different in longitudinal and cross subject task"""
    tsm.task_par['tsk_set']['reg']['mermaid_iter']['affine']={}
    """ settings for the mermaid-affine optimization version"""
    tsm.task_par['tsk_set']['reg']['mermaid_iter']['affine']['sigma'] =np.sqrt(0.5)
    tsm.task_par['tsk_set']['reg']['mermaid_iter']['use_init_weight'] =True
    tsm.task_par['tsk_set']['reg']['mermaid_iter']['weights_for_fg'] =[0.06666666666666667,
                                                                        0.13333333333333333,
                                                                        0.19999999999999998,
                                                                        0.26666666666666666,
                                                                        0.3333333333333333]
    tsm.task_par['tsk_set']['reg']['mermaid_iter']['weights_for_bg'] =[ 0,   0,   0,   0,   1]
    #tsm.task_par['tsk_set']['reg']['mermaid_iter']['multi_gaussian_stds'] =[ 0.05,0.10,0.15,0.20,0.25] # should be set in json file
    tsm.task_par['tsk_set']['reg']['mermaid_iter']['mermaid_affine_json'] ='../model_pool/cur_settings_affine_tmp.json'
    tsm.task_par['tsk_set']['reg']['mermaid_iter']['mermaid_nonp_json'] ='../mermaid_settings/cur_settings_adpt_lddmm_new_fix_wkw.json'
    """ for optimization-based mermaid recommand np.sqrt(1./batch_sz) for longitudinal, recommand np.sqrt(0.5/batch_sz) for cross-subject """
    """ for optimization-based mermaid recommand np.sqrt(1.) for longitudinal, recommand np.sqrt(0.5) for cross-subject """


force_setting(dm,tsm,output_path)


run_one_task()