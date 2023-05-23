# from typing import Pattern
import bpy
from bpy.types import Operator
# from . helper import Helper
from bpy_extras.io_utils import ImportHelper
# from bpy.props import StringProperty
# import json
import os,subprocess,sys,glob
# from shutil import copyfile,rmtree,move
from os.path import join
from .panel import *
import shutil

### TEST ###
import bpy
import os
import yaml
from bpy.props import StringProperty, FloatProperty, BoolProperty, IntProperty
from bpy.types import Operator, Panel, PropertyGroup
from ruamel.yaml import YAML
#############

def simple_gen_exec(context):

    econ_prop = context.scene.econ_prop

    path_addon = os.path.dirname(os.path.abspath(__file__))
    path_venv = econ_prop.str_venv_path
    path_venv_full = join(path_venv,econ_prop.str_custom_venv_name)
    path_venv_cuda = join(path_venv,econ_prop.str_custom_venv_name,'CUDA')
    path_venv_activate = join(path_venv_full,'Scripts','activate.bat')
    
    drive_addon = path_addon.split(':')[0]
    rest_path_addon = path_addon.split(':')[1]

    rest_path_stable_diffusion = join(rest_path_addon,'stable-diffusion-main')

    if os.path.exists(path_venv_activate):
        
        with open(path_venv_activate, "rt") as fin: #cria um bat com a ativacao do venv e inclui instalacao dos pacotes para Stable diffusion
            with open(join(path_addon,'install_econ_reqs_local.bat'), "wt") as fout:
                for line in fin:
                    # fout.write(line.replace('####RESULTS_DIR####', folder_prj))
                    fout.write(line)
                fout.write('\nrem %1 - drive env')
                fout.write('\nrem %2 - path to venv (wihtout drive)')
                fout.write('\nrem %3 - env_folder')


                fout.write('\n'+drive_addon+':')
                # fout.write('\ncd'+rest_path_stable_diffusion)
                fout.write('\ncd'+rest_path_addon)
                fout.write('\ncd')
                fout.write('\necho --------------------------------------------------')
                # fout.write('\npython -mpip install -r "'+join(path_addon,'stable-diffusion-main','requirements_test.txt"'))

                fout.write('\npython -mpip install -r requirements.txt')

                fout.write('\npython -mpip install src\\rembg-0+unknown-py3-none-any.whl')
                fout.write('\npython -mpip install src\\voxelize_cuda-0.0.0-cp38-cp38-win_amd64.whl')

                # # fout.write('\nset python_include=%3\\compilando\\Python\\include')
                # # fout.write('\nset python_pc=%3\\compilando\\Python\\PC')
                # # fout.write('\nset python_libs=%3\\compilando\\Python\\libs')
                # # fout.write('\nset INCLUDE=%python_pc%;%python_include%')
                # # fout.write('\nset LIB=%python_libs%')



                # # copiado do dreambooth
                # fout.write('\nset DISTUTILS_USE_SDK=1') #importante senao da erro "error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/"

                # # fout.write('\nset CUDA_HOME=%3\\compilando\\CUDA_v11.8')
                # # fout.write('\nset CUDA_PATH=%3\\compilando\\CUDA_v11.8')
                # # fout.write('\necho %CUDA_HOME%')
                
                # # fout.write('\nset PATH=%1:%2\\PortableGit\\cmd;%PATH%')


                # ## setting caminhos
                # # fout.write('\nset CUDA_PATH=%3\\compilando\\CUDA_v11.8')
                
                # fout.write('\nset python_include=%3\\compilando\\Python\\include')
                # fout.write('\nset python_pc=%3\\compilando\\Python\\PC')
                # fout.write('\nset python_libs=%3\\compilando\\Python\\libs')

                # # fout.write('\nset cuda_path=%3\\compilando\\CUDA_v11.8')
                # fout.write('\nset msvc_include=%3\\compilando\\MSVC\\include')
                # fout.write('\nset msvc_atlmfc_include=%3\\compilando\\MSVC\\ATLMFC\\include')
                # fout.write('\nset win_kit_include_ucrt=%3\\compilando\\MSVC\\windows_kits\\include\\ucrt')
                # fout.write('\nset win_kit_include_shared=%3\\compilando\\MSVC\\windows_kits\\include\\shared')
                # fout.write('\nset win_kit_include_um=%3\\compilando\\MSVC\\windows_kits\\include\\um')
                # fout.write('\nset win_kit_include_winrt=%3\\compilando\\MSVC\\windows_kits\\include\\winrt')
                # fout.write('\nset win_kit_include_cppwinrt=%3\\compilando\\MSVC\\windows_kits\\include\\cppwinrt')

                # fout.write('\nset msvc_atlmfc_lib=%3\\compilando\\MSVC\\ATLMFC\\lib\\x64')
                # fout.write('\nset msvc_lib=%3\\compilando\\MSVC\\lib\\x64')
                # fout.write('\nset win_kit_ucrt_lib=%3\\compilando\\windows_kits\\lib\\ucrt\\x64')
                # fout.write('\nset win_kit_um_lib=%3\\compilando\\windows_kits\\lib\\um\\x64')
                
                # fout.write('\nset win_kit_bin=%3\\compilando\\windows_kits\\bin\\10.0.19041.0\\x64')

                # fout.write('\nset todo_msvc_path=%3\\compilando\\FULL_COMMUNITY_MSVC\\2019\\Community\\VC\\Tools\\MSVC\\14.29.30133\\bin\\Hostx64\\x64')
                # fout.write('\nset ninja_path=%3\\compilando\\FULL_COMMUNITY_MSVC\\2019\\Community\\Common7\\IDE\\CommonExtensions\\Microsoft\\CMake\\Ninja')



                # # os.environ['CUDA_HOME'] = cuda_path
                # fout.write('\nset INCLUDE=%python_pc%;%python_include%;%win_kit_include_ucrt%;%msvc_include%;%msvc_atlmfc_include%;% win_kit_include_shared%;%win_kit_include_um%;%win_kit_include_winrt%;%win_kit_include_cppwinrt%')
                # fout.write('\nset LIB=%python_libs%;%msvc_atlmfc_lib%;%msvc_lib%;%win_kit_ucrt_lib%;%win_kit_um_lib%')
                # fout.write('\nset LIBPATH=%msvc_atlmfc_lib%;%msvc_lib%')
                # fout.write('\nset PATH=%win_kit_bin%;%CUDA_PATH%\\bin;%todo_msvc_path%;%ninja_path%;%PATH%')




                
                # fout.write('\ncd econ\\lib\\common\\libmesh')
                # # fout.write('\npython setup.py install')
                # fout.write('\npython setup.py build_ext --inplace')
                # fout.write('\ncd ..')
                

                # fout.write('\ncd libvoxelize')
                # # fout.write('\npython setup.py install')
                # fout.write('\npython setup.py build_ext --inplace')

                fout.write('\necho --------------------------------------------------------------')
                fout.write('\necho YOU CAN CLOSE THIS WINDOW NOW')
                fout.write('\necho --------------------------------------------------------------')
                
        print('Re created install_econ_reqs_local.bat')

        # with open(join(path_addon,'stable-diffusion-main','req_local.txt'), "wt") as fout:
        #     fout.write('\n-e '+join(path_venv_full,'src','taming-transformers')+'\\.')
        #     fout.write('\n-e '+join(path_venv_full,'src','CLIP')+'\\.')
        # print('Re created stable-diffusion-main/req_local.bat')

        with open(path_venv_activate, "rt") as fin: #cria um bat com a ativacao do venv e inclui instalacao dos pacotes para Stable diffusion
            with open(join(path_addon,'execute_python_generic.bat'), "wt") as fout:
                for line in fin:
                    # fout.write(line.replace('####RESULTS_DIR####', folder_prj))
                    fout.write(line)
                fout.write('\n'+drive_addon+':')
                fout.write('\ncd'+rest_path_stable_diffusion)

                fout.write('\nEcho path of the addon, execute')
                fout.write('\ncd')
                fout.write('\necho --------------------------------------------------')
                fout.write('\npython %*')
                # fout.write('\n%*')
        print('Re created execute_python_generic.bat')


        with open(path_venv_activate, "rt") as fin: #cria um bat com a ativacao do venv e inclui instalacao dos pacotes para Stable diffusion
            with open(join(path_addon,'execute_python_generic_custom_folder.bat'), "wt") as fout:
                for line in fin:
                    # fout.write(line.replace('####RESULTS_DIR####', folder_prj))
                    fout.write(line)
                fout.write('\nEcho path of the addon, execute')
                fout.write('\ncd')
                fout.write('\necho --------------------------------------------------')
                fout.write('\npython %*')
                # fout.write('\n%*')
        print('Re created execute_python_generic_custom_folder.bat')


class CreateVirtualEnviroment(Operator):

    bl_idname = "econ.create_virtual_env"
    bl_label = "Create ECON Venv"
    bl_description = "Create ECON Virtual Enviroment"

    def execute(self,context):

        import subprocess
        import sys

        econ_prop = context.scene.econ_prop
        path_addon = os.path.dirname(os.path.abspath(__file__))
        path_venv = econ_prop.str_venv_path
        env_folder_name = econ_prop.str_custom_venv_name
        path_pip_ini = join(path_venv,econ_prop.str_custom_venv_name,'pip.ini')

        drive_env = path_venv.split(':')[0]
        # rest_path_env = path_venv.split(':')[1]

        # install venv
        os.chdir(path_venv)#muda diretorio 
        if os.path.exists(join(path_venv,econ_prop.str_custom_venv_name)):
            print('Environment already created')
        else:
            subprocess.run([join(path_addon,'install_venv_p38.bat'),drive_env, path_addon , path_venv, env_folder_name]) #Cria o venv
        
        #arquivo criado para poder usar o pip pra instalar tudo de uma so vez
        with open(path_pip_ini, "wt") as fout:
            fout.write('[global]')
            fout.write('\nindex-url=https://pypi.org/simple')
            fout.write('\nextra-index-url=https://download.pytorch.org/whl/cu116')
        print('pip.ini file created')

        simple_gen_exec(context)

        #disable the button
        econ_prop.bool_step1_create_econ_venv = True
    

        return{'FINISHED'}


class InstallSTLOnVenv(Operator):

    bl_idname = "econ.install_econ_on_venv"
    bl_label = "Install ECON on venv"
    bl_description = "Install ECON Virtual Enviroment"

    def execute(self,context):

        path_addon = os.path.dirname(os.path.abspath(__file__))
        econ_prop = context.scene.econ_prop
        path_venv =join(econ_prop.str_venv_path,econ_prop.str_custom_venv_name)

        drive = path_venv.split(':')[0]
        rest_path = path_venv.split(':')[1]

        # os.system('start cmd /k \""'+join(path_addon,'install_econ_reqs_local.bat')+'" '+drive+' '+rest_path+' '+econ_prop.str_venv_path+'\"')
        subprocess.run([join(path_addon,'install_econ_reqs_local.bat'),drive, rest_path , econ_prop.str_venv_path]) #Cria o venv

        #desabilta o botao
        econ_prop.bool_step3_install_econ_venv = True
        return{'FINISHED'}



class FinishECONInstall(Operator):

    bl_idname = "econ.finish_econ_install"
    bl_label = "Finish ECON Install"
    bl_description = "Finish ECON Install"

    def execute(self,context):

        path_addon = os.path.dirname(os.path.abspath(__file__))
        econ_prop = context.scene.econ_prop
        path_venv =econ_prop.str_venv_path
        path_venv_full =join(econ_prop.str_venv_path,econ_prop.str_custom_venv_name)

        with open(join(path_addon,'finish_ECON_install.bat'), "wt") as fout:
            fout.write('call \"'+join(path_venv_full,'Scripts','activate.bat')+'\"')


            ## setting caminhos
            # fout.write('\nset CUDA_PATH=%3\\compilando\\CUDA_v11.8')
            
            fout.write('\nset python_include=%1\\compilando\\Python\\include')
            fout.write('\nset python_pc=%1\\compilando\\Python\\PC')
            fout.write('\nset python_libs=%1\\compilando\\Python\\libs')

            # fout.write('\nset cuda_path=%1\\compilando\\CUDA_v11.8')
            fout.write('\nset msvc_include=%1\\compilando\\MSVC\\include')
            fout.write('\nset msvc_atlmfc_include=%1\\compilando\\MSVC\\ATLMFC\\include')
            fout.write('\nset win_kit_include_ucrt=%1\\compilando\\MSVC\\windows_kits\\include\\ucrt')
            fout.write('\nset win_kit_include_shared=%1\\compilando\\MSVC\\windows_kits\\include\\shared')
            fout.write('\nset win_kit_include_um=%1\\compilando\\MSVC\\windows_kits\\include\\um')
            fout.write('\nset win_kit_include_winrt=%1\\compilando\\MSVC\\windows_kits\\include\\winrt')
            fout.write('\nset win_kit_include_cppwinrt=%1\\compilando\\MSVC\\windows_kits\\include\\cppwinrt')

            fout.write('\nset msvc_atlmfc_lib=%1\\compilando\\MSVC\\ATLMFC\\lib\\x64')
            fout.write('\nset msvc_lib=%1\\compilando\\MSVC\\lib\\x64')
            fout.write('\nset win_kit_ucrt_lib=%1\\compilando\\windows_kits\\lib\\ucrt\\x64')
            fout.write('\nset win_kit_um_lib=%1\\compilando\\windows_kits\\lib\\um\\x64')
            
            fout.write('\nset win_kit_bin=%1\\compilando\\windows_kits\\bin\\10.0.19041.0\\x64')

            fout.write('\nset todo_msvc_path=%1\\compilando\\FULL_COMMUNITY_MSVC\\2019\\Community\\VC\\Tools\\MSVC\\14.29.30133\\bin\\Hostx64\\x64')
            fout.write('\nset ninja_path=%1\\compilando\\FULL_COMMUNITY_MSVC\\2019\\Community\\Common7\\IDE\\CommonExtensions\\Microsoft\\CMake\\Ninja')



            # os.environ['CUDA_HOME'] = cuda_path
            fout.write('\nset INCLUDE=%python_pc%;%python_include%;%win_kit_include_ucrt%;%msvc_include%;%msvc_atlmfc_include%;% win_kit_include_shared%;%win_kit_include_um%;%win_kit_include_winrt%;%win_kit_include_cppwinrt%')
            fout.write('\nset LIB=%python_libs%;%msvc_atlmfc_lib%;%msvc_lib%;%win_kit_ucrt_lib%;%win_kit_um_lib%')
            fout.write('\nset LIBPATH=%msvc_atlmfc_lib%;%msvc_lib%')
            # fout.write('\nset PATH=%win_kit_bin%;%CUDA_PATH%\\bin;%todo_msvc_path%;%ninja_path%;%PATH%')
            fout.write('\nset PATH=%win_kit_bin%;%todo_msvc_path%;%ninja_path%;%PATH%')


            fout.write('\ncd econ\\lib\\common\\libmesh')
            # fout.write('\npython setup.py install')
            fout.write('\npython setup.py build_ext --inplace')
            fout.write('\ncd ..')
            

            fout.write('\ncd libvoxelize')
            # fout.write('\npython setup.py install')
            fout.write('\npython setup.py build_ext --inplace')
            

        current_folder = os.getcwd()
        os.chdir(path_addon)
        # os.system('start cmd /k \""'+join(path_addon,'install_pytorch3d.bat')+'" '+drive+' '+rest_path+' '+econ_prop.str_venv_path+'\"')
        # os.system('start cmd /k "'+join(path_addon,'finish_ECON_install.bat')+'" '+path_venv)
        subprocess.run([join(path_addon,'finish_ECON_install.bat'),path_venv]) #Cria o venv
        
        os.chdir(current_folder)


        #disable the button
        econ_prop.bool_step5_finish_econ=True


        

        return{'FINISHED'}


class VenvPathSelect(Operator, ImportHelper):
    bl_idname = "econ.venv_path_select"
    bl_label = "Venv Path"
    bl_description = "Select Venv Path"

    # filename_ext = ".ckpt"
    filter_glob: StringProperty(
        # default="*.ckpt",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    def execute(self,context):
        
        econ_prop = context.scene.econ_prop
        path_venv_path = os.path.dirname(self.filepath)
        econ_prop.str_venv_path = os.path.dirname(self.filepath)

        path_addon = os.path.dirname(os.path.abspath(__file__))
        path_venv_path_txt = join(path_addon,'venv_path.txt')

        with open(path_venv_path_txt, "wt") as fout:
            fout.write(path_venv_path)

        simple_gen_exec(context)

        return{'FINISHED'}

class InstallCompiler(Operator, ImportHelper):
    bl_idname = "econ.install_compiler"
    bl_label = "Install Compiler"
    bl_description = "Install Compiler"

    filename_ext = ".7z"
    filter_glob: StringProperty(
        default="*.7z",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    def execute(self,context):
        path_addon = os.path.dirname(os.path.abspath(__file__))
        econ_prop = context.scene.econ_prop
        compiler_zip = self.filepath
        destination = econ_prop.str_venv_path
        # destination = join(path_addon,'Text2Light','logs')

        if not os.path.exists(destination):
            os.makedirs(destination, exist_ok=True)

        # from pyunpack import Archive
        # Archive(compiler_zip).extractall(destination)
        #executing the process
        current_folder = os.getcwd()
        os.chdir(path_addon)
        subprocess.run([join(path_addon,'execute_python_generic_custom_folder.bat'),'unpack_7z.py', '-i',compiler_zip , '-o',destination])
        os.chdir(current_folder)

        #disable the button
        econ_prop.bool_step4_install_compiler=True

        return{'FINISHED'}


class ExecutePrompt(Operator):

    bl_idname = "text2light.execute"
    bl_label = "Execute Prompt"
    bl_description = "Execute Prompt"

    option: IntProperty(name='option') #1 para 4k, 2 para

    def execute(self,context):

        path_addon = os.path.dirname(os.path.abspath(__file__))
        econ_prop = context.scene.econ_prop
        


        current_folder = os.getcwd()
        os.chdir(join(path_addon,'Text2Light'))
        # subprocess.run([join(path_addon,'Execute_midas.bat')])
        if self.option ==1:
            subprocess.run([join(path_addon,'execute_python_generic_custom_folder.bat'),'text2light.py','-rg', 'logs/global_sampler_clip', '-rl', 'logs/local_sampler_outdoor', '--outdir', '../result', '--text', econ_prop.str_sd_prompt, '--clip', 'clip_emb.npy', '--sritmo', 'logs/sritmo.pth', '--sr_factor','4'])
        if self.option == 2:
            subprocess.run([join(path_addon,'execute_python_generic_custom_folder.bat'),'text2light.py','-rg', 'logs/global_sampler_clip', '-rl', 'logs/local_sampler_outdoor', '--outdir', '../result', '--text', econ_prop.str_sd_prompt, '--clip', 'clip_emb.npy'])
        

        os.chdir(current_folder)
        return{'FINISHED'}

class UseHDRI(Operator):

    bl_idname = "text2light.use_hdri"
    bl_label = "Use HDRI"
    bl_description = "Use last generated HDRI"

    def execute(self,context):

        path_addon = os.path.dirname(os.path.abspath(__file__))
        econ_prop = context.scene.econ_prop
        hdri = join(path_addon,'result','hdr','*.exr')
        
        result = sorted(glob.glob(hdri), key=os.path.getmtime)
        load_hdri = result[-1]

        scene = bpy.context.scene

        if scene.world is None:
            # create a new world
            new_world = bpy.data.worlds.new("Text2Light")
            scene.world = new_world
            bpy.context.scene.world.use_nodes = True
        else:
            for w in bpy.data.worlds:
                if w.name=='Text2Light':
                    scene.world = w
                
        #se apos o processo acima ainda nao existir world definido como text2light, criar um (pois algum deles falhou)
        if scene.world.name != "Text2Light":
            new_world = bpy.data.worlds.new("Text2Light")
            scene.world = new_world
            bpy.context.scene.world.use_nodes = True

        C = bpy.context
        scn = C.scene

        # Get the environment node tree of the current scene
        node_tree = scn.world.node_tree
        tree_nodes = node_tree.nodes

        # Clear all nodes
        tree_nodes.clear()

        # Add Background node
        node_background = tree_nodes.new(type='ShaderNodeBackground')

        # Add Environment Texture node
        node_environment = tree_nodes.new('ShaderNodeTexEnvironment')
        # Load and assign the image to the node property
        node_environment.image = bpy.data.images.load(load_hdri) # Relative path
        node_environment.location = -300,0

        # Add Output node
        node_output = tree_nodes.new(type='ShaderNodeOutputWorld')   
        node_output.location = 200,0

        # Link all nodes
        links = node_tree.links
        link = links.new(node_environment.outputs["Color"], node_background.inputs["Color"])
        link = links.new(node_background.outputs["Background"], node_output.inputs["Surface"])

        econ_prop.fl_bg_strength=1

        
        
        return{'FINISHED'}


class OpenOutputFolder(Operator):
    bl_idname = "text2light.open_output_folder"
    bl_label = "Open Output Folder"
    bl_description = "Open Output Folder"

    def execute(self,context):
        
        path_addon = os.path.dirname(os.path.abspath(__file__))

        
        output_folder = join(path_addon,'result','hdr')

        os.system('explorer "'+output_folder+'"')
        return{'FINISHED'}



class DownloadECON(Operator):
    bl_idname = "econ.download_econ"
    bl_label = "Download ECON"
    bl_description = "Download and Unzip ECON"

    def execute(self,context):
        
        path_addon = os.path.dirname(os.path.abspath(__file__))
        # OLD Jan 9 2023
        # archive_ref = '3b5ac63fd59b8c915235c62c981ead113c40d3b7'

        # NEW May 14 2023
        archive_ref = '6eec05720031c0a3fe008f00191ae4ef37d4dc00'
        # rename folder
        src = join(path_addon,'ECON-'+archive_ref)

        # Destination
        dest = join(path_addon,'ECON')

        if not os.path.exists(dest):
            import urllib.request
            url = 'https://github.com/YuliangXiu/ECON/archive/'+archive_ref+'.zip'
            download_path = join(path_addon,"ECON_github.zip")
            urllib.request.urlretrieve(url, download_path)

            # Unzip
            import zipfile
            with zipfile.ZipFile(download_path, 'r') as zip_ref:
                zip_ref.extractall(path_addon)


            # Renaming the file
            os.rename(src, dest)

            os.remove(download_path)

        #disable the button
        econ_prop = context.scene.econ_prop
        econ_prop.bool_step2_downlad_econ = True




        return{'FINISHED'}


class DownloadPytorch3d(Operator):
    bl_idname = "econ.download_pytorch3d"
    bl_label = "Down&Install Pytorch3D"
    bl_description = "Download and Install Pytorch3d"

    def execute(self,context):
        
        path_addon = os.path.dirname(os.path.abspath(__file__))
        econ_prop = context.scene.econ_prop
        path_venv = econ_prop.str_venv_path
        path_venv_full = join(path_venv,econ_prop.str_custom_venv_name)
        archive_ref = '3388d3f0aa6bc44fe704fca78d11743a0fcac38c'
        # rename folder
        src = join(path_venv_full,'pytorch3d-'+archive_ref)

        # Destination
        dest = join(path_venv_full,'pytorch3d')

        if not os.path.exists(dest):
            import urllib.request
            url = 'https://github.com/facebookresearch/pytorch3d/archive/'+archive_ref+'.zip'
            download_path = join(path_addon,"Pytorch3d_github.zip")
            urllib.request.urlretrieve(url, download_path)

            # Unzip
            import zipfile
            with zipfile.ZipFile(download_path, 'r') as zip_ref:
                zip_ref.extractall(path_venv_full)


            # Renaming the file
            os.rename(src, dest)



        with open(join(path_addon,'install_pytorch3d.bat'), "wt") as fout:
            fout.write('call \"'+join(path_venv_full,'Scripts','activate.bat')+'\"')


            ## setting caminhos
            # fout.write('\nset CUDA_PATH=%3\\compilando\\CUDA_v11.8')
            
            fout.write('\nset python_include=%1\\compilando\\Python\\include')
            fout.write('\nset python_pc=%1\\compilando\\Python\\PC')
            fout.write('\nset python_libs=%1\\compilando\\Python\\libs')

            # fout.write('\nset cuda_path=%1\\compilando\\CUDA_v11.8')
            fout.write('\nset msvc_include=%1\\compilando\\MSVC\\include')
            fout.write('\nset msvc_atlmfc_include=%1\\compilando\\MSVC\\ATLMFC\\include')
            fout.write('\nset win_kit_include_ucrt=%1\\compilando\\MSVC\\windows_kits\\include\\ucrt')
            fout.write('\nset win_kit_include_shared=%1\\compilando\\MSVC\\windows_kits\\include\\shared')
            fout.write('\nset win_kit_include_um=%1\\compilando\\MSVC\\windows_kits\\include\\um')
            fout.write('\nset win_kit_include_winrt=%1\\compilando\\MSVC\\windows_kits\\include\\winrt')
            fout.write('\nset win_kit_include_cppwinrt=%1\\compilando\\MSVC\\windows_kits\\include\\cppwinrt')

            fout.write('\nset msvc_atlmfc_lib=%1\\compilando\\MSVC\\ATLMFC\\lib\\x64')
            fout.write('\nset msvc_lib=%1\\compilando\\MSVC\\lib\\x64')
            fout.write('\nset win_kit_ucrt_lib=%1\\compilando\\windows_kits\\lib\\ucrt\\x64')
            fout.write('\nset win_kit_um_lib=%1\\compilando\\windows_kits\\lib\\um\\x64')
            
            fout.write('\nset win_kit_bin=%1\\compilando\\windows_kits\\bin\\10.0.19041.0\\x64')

            fout.write('\nset todo_msvc_path=%1\\compilando\\FULL_COMMUNITY_MSVC\\2019\\Community\\VC\\Tools\\MSVC\\14.29.30133\\bin\\Hostx64\\x64')
            fout.write('\nset ninja_path=%1\\compilando\\FULL_COMMUNITY_MSVC\\2019\\Community\\Common7\\IDE\\CommonExtensions\\Microsoft\\CMake\\Ninja')



            # os.environ['CUDA_HOME'] = cuda_path
            fout.write('\nset INCLUDE=%python_pc%;%python_include%;%win_kit_include_ucrt%;%msvc_include%;%msvc_atlmfc_include%;% win_kit_include_shared%;%win_kit_include_um%;%win_kit_include_winrt%;%win_kit_include_cppwinrt%')
            fout.write('\nset LIB=%python_libs%;%msvc_atlmfc_lib%;%msvc_lib%;%win_kit_ucrt_lib%;%win_kit_um_lib%')
            fout.write('\nset LIBPATH=%msvc_atlmfc_lib%;%msvc_lib%')
            # fout.write('\nset PATH=%win_kit_bin%;%CUDA_PATH%\\bin;%todo_msvc_path%;%ninja_path%;%PATH%')
            fout.write('\nset PATH=%win_kit_bin%;%todo_msvc_path%;%ninja_path%;%PATH%')


            fout.write('\npython setup.py install')

        current_folder = os.getcwd()
        os.chdir(dest)
        # os.system('start cmd /k \""'+join(path_addon,'install_pytorch3d.bat')+'" '+drive+' '+rest_path+' '+econ_prop.str_venv_path+'\"')
        # os.system('start cmd /k "'+join(path_addon,'install_pytorch3d.bat')+'" '+path_venv)
        subprocess.run([join(path_addon,'install_pytorch3d.bat'),path_venv]) #Cria o venv
        
        os.chdir(current_folder)

        #disable button
        econ_prop.bool_step6_install_pytorch = True


        return{'FINISHED'}

class ExeceteECON(Operator):
    bl_idname = "econ.execute_econ"
    bl_label = "Generate 3D Model"
    bl_description = "Generate 3D model from image"

    def execute(self,context):

        path_addon = os.path.dirname(os.path.abspath(__file__))
        econ_prop = context.scene.econ_prop
        path_venv = econ_prop.str_venv_path
        path_venv_full = join(path_venv,econ_prop.str_custom_venv_name)
        with open(join(path_addon,'execute_econ.bat'), "wt") as fout:
            fout.write('call \"'+join(path_venv_full,'Scripts','activate.bat')+'\"')
            fout.write('\npython -m apps.infer -cfg ./configs/econ.yaml -in_dir ./examples -out_dir ./results --loop_smpl 10')
            # fout.write('\npython -m apps.infer -cfg ./configs/econ.yaml -in_dir ./examples -out_dir ./results')

        result_folder = join(path_addon,'ECON','results','econ')

        bni = join(result_folder,'BNI','examples')
        obj = join(result_folder,'obj','examples')
        png = join(result_folder,'png','examples')
        vid = join(result_folder,'vid','examples')

        if not os.path.exists(bni):
            os.makedirs(bni)
        if not os.path.exists(obj):
            os.makedirs(obj)
        if not os.path.exists(png):
            os.makedirs(png)
        if not os.path.exists(vid):
            os.makedirs(vid)
        
        
        econ_folder = join(path_addon,'ECON')
        current_folder = os.getcwd()
        os.chdir(econ_folder)
        # os.system('start cmd /k \""'+join(path_addon,'install_pytorch3d.bat')+'" '+drive+' '+rest_path+' '+econ_prop.str_venv_path+'\"')
        # os.system('start cmd /k "'+join(path_addon,'execute_econ.bat')+'"')
        subprocess.run([join(path_addon,'execute_econ.bat')]) #Executa o ECON
        
        os.chdir(current_folder)


        #carrega obj no blender
        full_obj = join(result_folder,'obj','examples','*_full.obj')

        final_obj = sorted(glob.glob(full_obj), key=os.path.getmtime) #ordena os FULL.obj

        bpy.ops.wm.obj_import(filepath=final_obj[-1]) #import o ultimo


        return{'FINISHED'}


class LoadECONResult(Operator):
    bl_idname = "econ.load_econ"
    bl_label = "Load"
    bl_description = "Load"

    def execute(self,context):

        path_addon = os.path.dirname(os.path.abspath(__file__))
        econ_prop = context.scene.econ_prop
        path_venv = econ_prop.str_venv_path
        path_venv_full = join(path_venv,econ_prop.str_custom_venv_name)
        
        result_folder = join(path_addon,'ECON','results','econ')

        # full_obj = join(result_folder,'obj','examples','*.obj')
        full_obj = join(result_folder,'obj','examples','*_full.obj')

        final_obj = sorted(glob.glob(full_obj), key=os.path.getmtime)

        bpy.ops.wm.obj_import(filepath=final_obj[-1])
        # bpy.ops.wm.obj_import(filepath="D:\\0_Programs\\CEB_ECON_prj\\CEB_ECON\\ECON\\results\\econ\\obj\\examples\\304e9c4798a8c3967de7c74c24ef2e38_0_full.obj", directory="D:\\0_Programs\\CEB_ECON_prj\\CEB_ECON\\ECON\\results\\econ\\obj\\examples\\", files=[{"name":"304e9c4798a8c3967de7c74c24ef2e38_0_full.obj", "name":"304e9c4798a8c3967de7c74c24ef2e38_0_full.obj"}])


        return{'FINISHED'}
    
############################ TEST ######################################

class ECON_SaveConfig(Operator):
    bl_idname = "econ.save_config"
    bl_label = "Save Configuration"

    def execute(self, context):
        path_addon = os.path.dirname(os.path.abspath(__file__))
        econ_prop = context.scene.econ_prop
        config_path = os.path.join(path_addon, "ECON", "configs", "econ.yaml")

        yaml = YAML(typ='rt')  # Round trip loading and dumping
        with open(config_path, 'r') as f:
            data = yaml.load(f)
        
        use_smpl = [bpy.context.scene.econ_prop.use_smpl_hand, bpy.context.scene.econ_prop.use_smpl_face]
        use_smpl_data = []
        use_smpl_mapping = ["hand", "face"]
        for i, flag in enumerate(use_smpl):
            if flag:
                use_smpl_data.append(use_smpl_mapping[i])
        data['bni']['use_smpl'] = use_smpl_data
        data['bni']['thickness'] = float(econ_prop.thickness)
        data['bni']['k'] = int(econ_prop.k)
        data['bni']['hps_type'] = econ_prop.hps_type
        data['bni']['texture_src'] = econ_prop.texture_src
        data['bni']['use_ifnet'] = econ_prop.use_ifnet

        with open(config_path, 'w') as f:
            yaml.dump(data, f)

        self.report({'INFO'}, "Configuration saved")
        return {'FINISHED'}


# class ShowVertexColorTexture(bpy.types.Operator):
#     bl_idname = "object.show_vertex_color_texture"
#     bl_label = "View Vertex Color Texture"

#     def execute(self, context):
#         active_obj = bpy.context.active_object

#         if not active_obj or active_obj.type != 'MESH':
#             self.report({'ERROR'}, 'Active object is not a mesh object')
#             return {'CANCELLED'}

#         # Check if color attributes exist
#         if 'Color' not in active_obj.data.attributes:
#             self.report({'ERROR'}, 'No vertex color data found on the active object')
#             return {'CANCELLED'}

#         mat = bpy.data.materials.new(name="VertexColMat")
#         mat.use_nodes = True

#         # Try to get Principled BSDF node
#         bsdf_node = mat.node_tree.nodes.get("Principled BSDF")
#         # Create a new one if not found
#         if bsdf_node is None:
#             bsdf_node = mat.node_tree.nodes.new('ShaderNodeBsdfPrincipled')

#         # Create an attribute node and set it to 'Color'
#         attr_node = mat.node_tree.nodes.new('ShaderNodeAttribute')
#         attr_node.attribute_name = 'Color'
#         mat.node_tree.links.new(bsdf_node.inputs['Base Color'], attr_node.outputs['Color'])

#         # Assign it to active object
#         if active_obj.data.materials:
#             active_obj.data.materials[0] = mat
#         else:
#             active_obj.data.materials.append(mat)

#         return {'FINISHED'}
###########################################################################################################

class ImportImage(Operator, ImportHelper):
    bl_idname = "econ.import_image"
    bl_label = "Import Image"
    bl_description = "Import Image to Process"

    # filename_ext = ".7z"
    filter_glob: StringProperty(
        default="*.jpg;*.jpeg;*.png;*.bmp;*.exr;*.tiff",
        # options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    def execute(self,context):

        path_addon = os.path.dirname(os.path.abspath(__file__))
        econ_prop = context.scene.econ_prop
        path_venv = econ_prop.str_venv_path
        path_venv_full = join(path_venv,econ_prop.str_custom_venv_name)
        
        img_folder = join(path_addon,'ECON','examples')


        src = self.filepath

        name_file = os.path.basename(src)

        dst = join(img_folder,name_file)

        if os.path.exists(img_folder):
            shutil.rmtree(img_folder)
            os.makedirs(img_folder)


        shutil.copyfile(src, dst)

        return{'FINISHED'}
    
class CurrentImage(Operator):
    bl_idname = "econ.Current_image"
    bl_label = "Current Image"
    bl_description = "Current Image File Name"


def down_smpl_file(context,url,destination,down_file):
    import requests
    path_addon = os.path.dirname(os.path.abspath(__file__))
    econ_prop = context.scene.econ_prop
    payload = {"username":econ_prop.str_smpl_username,
            "password": econ_prop.str_smpl_password,
            }
    r = requests.post(url, data=payload)

    if not os.path.exists(destination):
        os.makedirs(destination, exist_ok=True)
    
    final_file = join(destination,down_file)

    if r.status_code == 200:
        with open(final_file,"wb") as f:
            f.write(r.content)


class DownloadModels(Operator):
    bl_idname = "econ.download_models"
    bl_label = "Download"
    bl_description = "Download"

    def execute(self,context):
        from zipfile import ZipFile

        path_addon = os.path.dirname(os.path.abspath(__file__))
        econ_prop = context.scene.econ_prop

        destination = join(path_addon,'data_temp')

        # shutil.rmtree(destination)

        
        # START ############### File SMPL_python_v.1.0.0.zip
        ################
        down_file = "SMPL_python_v.1.0.0.zip"
        print('In: ',down_file)

        destination = join(path_addon,'data_temp')
        url = "https://download.is.tue.mpg.de/download.php?domain=smpl&sfile=SMPL_python_v.1.0.0.zip&resume=1"

        unzip_file = join(destination,down_file)
        if not os.path.exists(unzip_file):
            down_smpl_file(context,url,destination,down_file)
            print('Downloaded:',down_file)

        #unzipping 
        name_f = 'basicModel_f_lbs_10_207_0_v1.0.0.pkl'
        name_m = 'basicmodel_m_lbs_10_207_0_v1.0.0.pkl'
        extract_f = join('smpl','models',name_f)
        extract_m = join('smpl','models',name_m)

        end_folder_f = join(path_addon,'ECON','data','smpl_related','models','smpl')
        end_folder_m = join(path_addon,'ECON','data','smpl_related','models','smpl')
        end_file_f_default = join(end_folder_f,name_f)
        end_file_m_default = join(end_folder_m,name_m)
        end_file_f = join(end_folder_f,'SMPL_FEMALE.pkl')
        end_file_m = join(end_folder_m,'SMPL_MALE.pkl')

        with ZipFile(unzip_file, 'r') as zObject:
            if not os.path.exists(end_file_f):
                zObject.extract(extract_f.replace('\\','/'), path=destination)
            if not os.path.exists(end_file_m):
                zObject.extract(extract_m.replace('\\','/'), path=destination)
        zObject.close()

        os.makedirs(end_folder_f,exist_ok=True)
        os.makedirs(end_folder_m,exist_ok=True)
        if not os.path.exists(end_file_f):
            shutil.move(join(destination,extract_f),end_file_f_default)
        if not os.path.exists(end_file_m):
            shutil.move(join(destination,extract_m),end_file_m_default)

        #rename
        if not os.path.exists(end_file_f):
            os.rename(end_file_f_default,end_file_f)
        if not os.path.exists(end_file_f):
            os.rename(end_file_m_default,end_file_m)

        #removing files zipped file
        if econ_prop.bool_erase_zip:
            os.remove(unzip_file)
        #removing folder
        destination_to_erase = join(destination,'smpl')
        if os.path.exists(destination_to_erase):
            shutil.rmtree(destination_to_erase)
            print('Unzipped:',down_file)
        print('Out: ',down_file)
        ################
        # END ################ File SMPL_python_v.1.0.0.zip
        



        
        # START ############### FILE :  mpips_smplify_public_v2.zip
        ################
        down_file = 'mpips_smplify_public_v2.zip'
        print('In: ',down_file)

        destination = join(path_addon,'data_temp')
        url = 'https://download.is.tue.mpg.de/download.php?domain=smplify&sfile=mpips_smplify_public_v2.zip&resume=1' 
        unzip_file = join(destination,down_file)
        if not os.path.exists(unzip_file):
            down_smpl_file(context,url,destination,down_file)
            print('Downloaded:',down_file)

        #unzipping 
        name_n = 'basicModel_neutral_lbs_10_207_0_v1.0.0.pkl'
        
        extract_n = join('smplify_public','code','models',name_n)

        end_folder_n = join(path_addon,'ECON','data','smpl_related','models','smpl')

        end_file_n_default = join(end_folder_n,name_n)
        end_file_n = join(end_folder_n,'SMPL_NEUTRAL.pkl')

        with ZipFile(unzip_file, 'r') as zObject:
            if not os.path.exists(end_file_n):
                zObject.extract(extract_n.replace('\\','/'), path=destination)
        zObject.close()

        os.makedirs(end_folder_n,exist_ok=True)
        
        if not os.path.exists(end_file_n):
            shutil.move(join(destination,extract_n),end_file_n_default)
        

        #rename
        if not os.path.exists(end_file_n):
            os.rename(end_file_n_default,end_file_n)

        #removing files zipped file
        if econ_prop.bool_erase_zip:
            os.remove(unzip_file)
        #removing folder
        destination_to_erase = join(destination,'smplify_public')
        if os.path.exists(destination_to_erase):
            shutil.rmtree(destination_to_erase)
            print('Unzipped:',down_file)
        print('Out: ',down_file)
        
        ################
        # END ################ File mpips_smplify_public_v2.zip
        


        # START ############### FILE :  models_smplx_v1_1.zip
        ################
        down_file = 'models_smplx_v1_1.zip'
        print('In: ',down_file)

        destination = join(path_addon,'data_temp')
        url = 'https://download.is.tue.mpg.de/download.php?domain=smplx&sfile=models_smplx_v1_1.zip&resume=1'
        unzip_file = join(destination,down_file)
        if not os.path.exists(unzip_file):
            down_smpl_file(context,url,destination,down_file)
            print('Downloaded:',down_file)

        #unzipping 

        names_to_extract = ['smplx_npz.zip','SMPLX_FEMALE.npz','SMPLX_FEMALE.pkl','SMPLX_MALE.npz','SMPLX_MALE.pkl','SMPLX_NEUTRAL.npz','SMPLX_NEUTRAL.pkl','version.txt']
        
        end_folder_n = join(path_addon,'ECON','data','smpl_related','models','smplx')
        
        with ZipFile(unzip_file, 'r') as zObject:
            for name in names_to_extract:
                extract_n = join('models','smplx',name)
                if not os.path.exists(join(end_folder_n,name)):
                    zObject.extract(extract_n.replace('\\','/'), path=destination)
        zObject.close()


        os.makedirs(end_folder_n,exist_ok=True)
        
        
        for name in names_to_extract:
            if not os.path.exists(join(end_folder_n,name)):
                shutil.move(join(destination,'models','smplx',name),join(end_folder_n,name))
        
        #removing files zipped file
        if econ_prop.bool_erase_zip:
            os.remove(unzip_file)
        #removing folder
        destination_to_erase = join(destination,'models','smplx')
        if os.path.exists(destination_to_erase):
            shutil.rmtree(destination_to_erase)
            print('Unzipped:',down_file)
        print('Out: ',down_file)
        
        ################
        # END ################ File mpips_smplify_public_v2.zip
        


        
        # START ############### FILE :  econ_data.zip
        ################
        down_file = 'econ_data.zip'
        print('In: ',down_file)

        destination = join(path_addon,'data_temp')
        url = 'https://download.is.tue.mpg.de/download.php?domain=icon&sfile=econ_data.zip&resume=1'
        unzip_file = join(destination,down_file)
        if not os.path.exists(unzip_file):
            down_smpl_file(context,url,destination,down_file)
            print('Downloaded:',down_file)

        #unzipping 
        extract_all = join(path_addon,'ECON','data')
        #move folder smpl_data
        source_folder = join(extract_all,'smpl_data')
        destination_folder = join(extract_all,'smpl_related','smpl_data')
        
        with ZipFile(unzip_file, 'r') as zObject:
            if not os.path.exists(destination_folder):
                zObject.extractall(path=extract_all)
        zObject.close()



        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            # fetch all files
            for file_name in os.listdir(source_folder):
                # construct full file path
                source = join(source_folder,file_name)
                destination = join(destination_folder, file_name)
                # move only files
                if os.path.isfile(source):
                    shutil.move(source, destination)
                    print('Moved:', file_name)

        #removing files zipped file
        if econ_prop.bool_erase_zip:
            os.remove(unzip_file)
            print('Unzipped:',down_file)
        print('Out: ',down_file)
        
        ################
        # END ################ File econ_data.zip
        

        
        # START ############### FILE :  pixie_data.zip
        ################
        down_file = 'pixie_data.zip'
        print('In: ',down_file)

        destination = join(path_addon,'data_temp')
        url = 'https://download.is.tue.mpg.de/download.php?domain=icon&sfile=HPS/pixie_data.zip&resume=1' 
        unzip_file = join(destination,down_file)
        if not os.path.exists(unzip_file):
            down_smpl_file(context,url,destination,down_file)
            print('Downloaded:',down_file)

        #unzipping 
        extract_all = join(path_addon,'ECON','data','HPS')
        check_end_folder = join(extract_all,'pixie_data')
        with ZipFile(unzip_file, 'r') as zObject:
            if not os.path.exists(check_end_folder):
                zObject.extractall(path=extract_all)
        zObject.close()

        #removing files zipped file
        if econ_prop.bool_erase_zip:
            os.remove(unzip_file)
            print('Unzipped:',down_file)
        print('Out: ',down_file)
        
        ################
        # END ################ File pixie_data.zip
        

        
        # START ############### FILE :  pymafx_data.zip
        ################
        down_file = 'pymafx_data.zip'
        print('In: ',down_file)

        destination = join(path_addon,'data_temp')
        url = 'https://download.is.tue.mpg.de/download.php?domain=icon&sfile=HPS/pymafx_data.zip&resume=1'
        unzip_file = join(destination,down_file)
        if not os.path.exists(unzip_file):
            down_smpl_file(context,url,destination,down_file)
            print('Downloaded:',down_file)

        #unzipping 
        extract_all = join(path_addon,'ECON','data','HPS')
        check_end_folder = join(extract_all,'pymafx_data')
        
        with ZipFile(unzip_file, 'r') as zObject:
            if not os.path.exists(check_end_folder):
                zObject.extractall(path=extract_all)
        zObject.close()

        #removing files zipped file
        if econ_prop.bool_erase_zip:
            os.remove(unzip_file)
            print('Unzipped:',down_file)
        print('Out: ',down_file)
        
        ################
        # END ################ File pymafx_data.zip

        return{'FINISHED'}


class EnableButton(Operator):
    bl_idname = "econ.enable_button"
    bl_label = "Enable"
    bl_description = "Enable"

    button: StringProperty(name='Button bool parameter')

    def execute(self,context):

        econ_prop = context.scene.econ_prop
        
        # econ_prop.bool_step1_create_econ_venv = False
        exec('econ_prop.'+self.button+'=False')


        return{'FINISHED'}


class OpenBlenderWithConsole(Operator):

    bl_idname = "econ.open_blender_with_console"
    bl_label = "Blender w/ Console"
    bl_description = "Open Blender With Console"

    def execute(self,context):

        os.system('start cmd /k "'+bpy.app.binary_path+'" -con')

        return{'FINISHED'}
