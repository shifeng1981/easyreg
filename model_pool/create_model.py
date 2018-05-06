import torch
def create_model(opt):
    model = None
    model_name = opt['tsk_set']['model']
    gpu_id = opt['tsk_set']['gpu_ids']
    sz = opt
    torch.cuda.set_device(gpu_id)
    print(model_name)
    if model_name == 'context_net':
        from .context_net import ContextNet
        model = ContextNet()
    elif model_name == 'unet':
        from .unet import Unet
        model = Unet()
    elif model_name == 'vonet':
        from .vonet import Vonet
        model = Vonet()
    elif model_name == 'pnet':
        from .pnet import Pnet
        model = Pnet()
    elif model_name == 'asm_net_test':
        from .assemble_net import Asm_test
        model = Asm_test()

    elif model_name == 'reg_net':
        from .reg_net import RegNet
        model = RegNet()
    elif opt.model == 'test':
        # from .test_model import TestModel
        # model = TestModel()
        pass
    else:
        raise ValueError("Model [%s] not recognized." % model_name)
    model.initialize(opt)
    print("model [%s] was created" % (model.name()))
    return model