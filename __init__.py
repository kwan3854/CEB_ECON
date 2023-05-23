import bpy
from bpy.props import (PointerProperty)
from .econ_blender import *
from . panel import *


bl_info = {
    "name" : "CEB ECON",
    "author" : "YuliangXiu, Carlos Barreto",
    "description" : "",
    "blender" : (3, 3, 1),
    "version" : (0, 10, 7),
    "location" : "UI > SidePanel",
    "warning" : "",
    "category" : "General"
}





classes = (ECONMySettings,ECON_PT_installation_panel
    ,CreateVirtualEnviroment,InstallSTLOnVenv,VenvPathSelect,InstallCompiler,ExecutePrompt
    ,UseHDRI,OpenOutputFolder

    ,DownloadECON,DownloadPytorch3d,ExeceteECON,LoadECONResult,ImportImage,DownloadModels,FinishECONInstall
    ,EnableButton,OpenBlenderWithConsole
    
    ,ECON_SaveConfig, ECON_PT_generatation_panel, LoadAvatarizerResult)
    # ,ShowVertexColorTexture)




def register():

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.econ_prop = PointerProperty(type=ECONMySettings)
    bpy.types.Scene.ceb_econ_img_path = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.ceb_econ_venv = bpy.props.BoolProperty(default=False)

    

def unregister():
    from bpy.utils import unregister_class


    for cls in reversed(classes):
        unregister_class(cls) 
    del bpy.types.Scene.econ_prop
    del bpy.types.Scene.ceb_econ_img_path
    del bpy.types.Scene.ceb_econ_venv


if __name__ == "__main__":
    register()
    