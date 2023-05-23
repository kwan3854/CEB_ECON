# from typing import Text
# from ctypes import alignment
# from unittest.mock import DEFAULT
import bpy,os,glob
from os.path import join
import sys
import textwrap
global DEFAULT_NAME
DEFAULT_NAME = 'ECON_38_env'

def update_venv_name_from_list(self,context):
    global DEFAULT_NAME
    econ_prop = context.scene.econ_prop
    # folder = econ_prop.str_sd_prompt.strip().replace(' ','_')
    folder = econ_prop.enum_custom_venv_list

    if folder == '-1':
        # econ_prop.str_custom_venv_name = 'text2light_39_env'
        econ_prop.str_custom_venv_name = DEFAULT_NAME
    if folder > '0': #0 é o que chamo the Nothing no panel
        econ_prop.str_custom_venv_name = folder

def _label_multiline(context, text, parent):
    chars = int(context.region.width / 7)   # 7 pix on 1 character
    wrapper = textwrap.TextWrapper(width=chars)
    text_lines = wrapper.wrap(text=text)
    for text_line in text_lines:
        parent.label(text=text_line)

def updt_custom_venv_name(self,context):
    econ_prop = context.scene.econ_prop
    custom_venv_name = econ_prop.str_custom_venv_name
    path_addon = os.path.dirname(os.path.abspath(__file__))
    custom_path_txt = join(path_addon,'custom_path.txt')
    with open(custom_path_txt, "wt") as fout_custom:
        fout_custom.write(custom_venv_name)

def updt_bool_custom_venv(self,context):
    global DEFAULT_NAME
    econ_prop = context.scene.econ_prop
    # wm = context.window_manager
    if not self.bool_custom_venv:
        econ_prop.str_custom_venv_name = DEFAULT_NAME

def updt_bool_venv_custom_name(self,context):
    econ_prop = context.scene.econ_prop
    # wm = context.window_manager
    if self.bool_custom_venv_name:
        econ_prop.bool_custom_venv_name_from_list = False   
def updt_bool_venv_custom_name_from_list(self,context):
    econ_prop = context.scene.econ_prop
    # wm = context.window_manager
    if self.bool_custom_venv_name_from_list:
        econ_prop.bool_custom_venv_name= False  

def folder_venv_callback(scene, context):
    econ_prop = context.scene.econ_prop
    directory = econ_prop.str_venv_path
    

    if os.path.exists(directory):
        folders = []
        # for root, dirs, files in os.walk(directory):
        for name_file_dir in os.listdir(directory):
            if os.path.isdir(join(directory,name_file_dir)) and name_file_dir.endswith('_39_env'):
                folders.append(name_file_dir)

        # list_folder = folders[0]
        list_folder = folders
        # print(list_folder)
        
        items = []
        i=0

        ####
        #generate the custom size to search for Constraint name (to be able to use "startswith")
        # len_name_start_ctr = len(name+'-{:03}'.format(0))
        items.append(("-1","Choose a Folder","Choose a Folder"))
        for x in range(len(list_folder)):
            i=i+1
            items.append((list_folder[x],"%s" % list_folder[x],"Data: %s" % list_folder[x]))
        if len(items) == 0:
            items.append((str(0),"Nothing","No Data available"))
    else:
        items = [(str(0),"Nothing","No Data available")]
        
    return items

def update_bg_strength(self,context):
    bpy.data.worlds["Text2Light"].node_tree.nodes["Background"].inputs[1].default_value = self.fl_bg_strength

### TEST ###
class ECON_PT_generatation_panel(bpy.types.Panel):
    bl_label = "Model Generation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ECON Generate Models'

    def draw(self, context):
        layout = self.layout
        econ_prop = context.scene.econ_prop

        rowA = layout.row(align=True).box()
        rowA.label(text='ECON Settings')
        rowA.prop(econ_prop, "use_smpl_hand", index=0, text="Use SMPL Hand")
        rowA.prop(econ_prop, "use_smpl_face", index=1, text="Use SMPL Face")
        rowA.prop(econ_prop, "thickness")
        rowA.prop(econ_prop, "k")
        rowA.prop(econ_prop, "hps_type")
        rowA.prop(econ_prop, "texture_src")
        rowA.prop(econ_prop, "use_ifnet")
        rowA.operator("econ.save_config")

        rowB = layout.row(align=True).box()
        rowB = rowB.column(align=True)
        rowB.label(text='Generate Models')
        rowB.label(text='Selected Image: ' + context.scene.econ_prop.selected_image)
        rowB.operator('econ.import_image')
        rowB.separator()
        rowB.operator('econ.execute_econ')

        # layout.operator("object.show_vertex_color_texture")

######################

class ECON_PT_installation_panel(bpy.types.Panel):
    bl_idname = "CEB_PT_ECON"
    bl_label = "ECON"
    bl_category = "ECON Install"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    
    def draw(self, context):

        layout = self.layout
        scene = context.scene
        econ_prop = context.scene.econ_prop

        path_venv = join(econ_prop.str_venv_path,econ_prop.str_custom_venv_name)
        flag_installed = join(econ_prop.str_venv_path,econ_prop.str_custom_venv_name,'Lib','site-packages','torch')

        # row.operator('econ.load_econ')
        
        # row.prop(econ_prop,'str_sd_prompt')
        # row.separator()
        # row.operator('text2light.execute',text='Execute 4K').option = 1
        # # row.operator('text2light.execute',text='Execute 0.5K').option = 2
        # row.operator('text2light.use_hdri')
        # row.prop(econ_prop,'fl_bg_strength')
        # _label_multiline(
        #     context=context,
        #     text='Full Prompt: '+econ_prop.str_sd_prompt,
        #     parent=row
        #     )
        # row.operator('text2light.open_output_folder')
        
           
        # row = layout.box()
        # row = row.column(align=True)
        # row_sub = row.column(align=True)
        # row_sub.label(text='Type of Process')
        
        
        rowb = layout.row(align=True).box()
        rowb = rowb.column(align=True)
        row = rowb.row(align=True)
        # row.enabled = enable_ctr
        row.enabled = True
        row.prop(scene, "ceb_econ_venv",
        icon="TRIA_DOWN" if scene.ceb_econ_venv else "TRIA_RIGHT",
        icon_only=True, emboss=False
        )
        row_alert_create_venv = row.column(align=True)
        if os.path.exists(path_venv):
            row_alert_create_venv.alert = False
        else:
            row_alert_create_venv.alert = True
        row_alert_create_venv.label(text='Venv and Installs') 


        if scene.ceb_econ_venv:
            row = rowb.column(align=True)
            
            

            row_path = row.row(align=True)
            row_path2 = row.row(align=True)
            
            if os.path.exists(econ_prop.str_venv_path):
                row_path.alert = False
                row_path2.alert = False
            else:
                row_path.alert = True
                row_path2.alert = True
                row_path.label(text='Select a valid Path')
            
            
            row_subpath = row.column(align=True)
            if ' ' in path_venv:
                # row_path2.alert = True
                row_subpath.alert=True
            else:
                # row_path2.alert = False
                row_subpath.alert=False
            row_path2.prop(econ_prop,'str_venv_path',text = '')
            row_path2.operator('econ.venv_path_select',text = 'Path')
            _label_multiline(
            context=context,
            text='Full Path: '+path_venv,
            parent=row_subpath
            )
            
            row_subpath.prop(econ_prop,'bool_custom_venv')
            if econ_prop.bool_custom_venv:
                row_subpath = row_subpath.row(align=True)
                row_subpath.prop(econ_prop,'bool_custom_venv_name',text='Name',toggle=1)
                row_subpath.prop(econ_prop,'bool_custom_venv_name_from_list',text='List',toggle=1)

                if econ_prop.bool_custom_venv_name:
                    row_sub_subpath = row.column(align=True)
                    # row_subpath = row_subpath.column(align=True)
                    row_sub_subpath.prop(econ_prop,'str_custom_venv_name',text='Name')
                if econ_prop.bool_custom_venv_name_from_list:
                    row_sub_subpath = row.column(align=True)
                    # row_subpath = row_subpath.column(align=True)
                    row_sub_subpath.prop(econ_prop,'enum_custom_venv_list',text='Folder')

            row.separator()
            row.separator()
            row = layout.row().box()
            row = row.column(align=True)
            row.operator('econ.open_blender_with_console')
            row.operator('wm.url_open',text='Get/Install 7zip',icon='URL').url = 'https://www.7-zip.org/download.html'
            _label_multiline(
                context=context,
                text='Get 7zip in case you dont have it, its needed to install the compiler',
                parent=row
            )
            row = layout.row().box()
            row = row.column(align=True)

            if ' ' in path_venv:
                row_space_alert = row_subpath.column(align=True)
                row_space_alert.alert = True
                row_space_alert.label(text='Choose a Path with no SPACE')
            else:
                row.separator()
                row_sub = row.row()
                row_step1 = row_sub.row()
                row_sub_step1 = row_sub.row()
                row_sub_step1.scale_x=0.5
                if econ_prop.bool_step1_create_econ_venv:
                    row_step1.enabled = False
                    row_step1.operator('econ.create_virtual_env')
                    row_sub_step1.operator('econ.enable_button').button='bool_step1_create_econ_venv'
                else:
                    row_step1.enabled = True
                    row_step1.operator('econ.create_virtual_env')


            row = layout.row(align=True).box()
            row = row.column(align=True)
            row.label(text='Compiler & Download ECON')
            row_sub = row.row()
            row_step2 = row_sub.row()
            row_sub_step2 = row_sub.row()
            row_sub_step2.scale_x=0.5
            if econ_prop.bool_step2_downlad_econ:
                row_step2.enabled = False
                row_step2.operator('econ.download_econ')
                row_sub_step2.operator('econ.enable_button').button='bool_step2_downlad_econ'
            else:
                row_step2.enabled = True
                row_step2.operator('econ.download_econ')

            row = layout.row().box()
            row_sub = row.column(align=True)

            row_alert_inst_venv_py = row_sub.column(align=True)
            row_alert_create_venv = row_sub.column(align=True)
            row_alert_install_sd_venv = row_sub.column(align=True)
            # row_alert_install_compiler = row_sub.column(align=True)
            # if not os.path.exists(path_venv_pypack):
            #     row_alert_inst_venv_py.alert = True
            # else:
            #     row_alert_inst_venv_py.alert = False

            if not os.path.exists(path_venv):
                row_alert_create_venv.alert = True
                row_alert_install_sd_venv.enabled = False
            else:
                row_alert_create_venv.alert = False
                row_alert_install_sd_venv.enabled = True

            # if not os.path.exists(flag_installed):
            #     row_alert_install_sd_venv.alert = True
            # else:
            #     row_alert_install_sd_venv.alert = False
            
          
            if ' ' in path_venv:
                row_space_alert = row_sub.column(align=True)
                row_space_alert.alert = True
                row_space_alert.label(text='Choose a Path with no SPACE')
            else:
                row_sub = row.row()
                row_step3 = row_sub.row()
                row_sub_step3 = row_sub.row()
                row_sub_step3.scale_x=0.5
                if econ_prop.bool_step3_install_econ_venv:
                    row_step3.enabled = False
                    row_step3.operator('econ.install_econ_on_venv')
                    row_sub_step3.operator('econ.enable_button').button='bool_step3_install_econ_venv'
                else:
                    row_step3.enabled = True
                    row_step3.operator('econ.install_econ_on_venv')

            row_sub = row.row()
            row_step4 = row_sub.row()
            row_sub_step4 = row_sub.row()
            row_sub_step4.scale_x=0.5
            if econ_prop.bool_step4_install_compiler:
                row_step4.enabled = False
                row_step4.operator('econ.install_compiler')
                row_sub_step4.operator('econ.enable_button').button='bool_step4_install_compiler'
            else:
                row_step4.enabled = True
                row_step4.operator('econ.install_compiler')

                
            row_sub = row.row()
            row_step5 = row_sub.row()
            row_sub_step5 = row_sub.row()
            row_sub_step5.scale_x=0.5
            if econ_prop.bool_step5_finish_econ:
                row_step5.enabled = False
                row_step5.operator('econ.finish_econ_install')
                row_sub_step5.operator('econ.enable_button').button='bool_step5_finish_econ'
            else:
                row_step5.enabled = True
                row_step5.operator('econ.finish_econ_install')



            row = layout.row(align=True).box()
            row = row.column(align=True)
            row.label(text='Install Pytorch3D')
            
            row_sub = row.row()
            row_step6 = row_sub.row()
            row_sub_step6 = row_sub.row()
            row_sub_step6.scale_x=0.5
            if econ_prop.bool_step6_install_pytorch:
                row_step6.enabled = False
                row_step6.operator('econ.download_pytorch3d')
                row_sub_step6.operator('econ.enable_button').button='bool_step6_install_pytorch'
            else:
                row_step6.enabled = True
                row_step6.operator('econ.download_pytorch3d')
           

            
            
            
            

            row = layout.row(align=True).box()
            row = row.column(align=True)
            row.label(text='Download Models')
            row.operator('wm.url_open',text='Register',icon='URL').url = 'https://icon.is.tue.mpg.de/'
            row.separator()
            
            _label_multiline(
                context=context,
                text='After registering, click on the link below and click on "Register Now" for all the options',
                parent=row
            )
            row.operator('wm.url_open',text='Register on all ',icon='URL').url = 'https://icon.is.tue.mpg.de/user.php'

            row.label(text='Login')
            row.prop(econ_prop,'str_smpl_username')
            row.prop(econ_prop,'str_smpl_password')
            row.operator('econ.download_models')
            row.prop(econ_prop,'bool_erase_zip')



   
from bpy.props import (StringProperty,
                       BoolProperty,
                      FloatProperty,
                      IntProperty,
                      BoolVectorProperty,
                        EnumProperty
                       )
from bpy.types import (PropertyGroup)

class ECONMySettings(PropertyGroup):
    global DEFAULT_NAME
    #venv Path
    path_addon = os.path.dirname(os.path.abspath(__file__))
    path_venv_path_txt = join(path_addon,'venv_path.txt')
    env_has_path_txt = 0
    if os.path.exists(path_venv_path_txt):
        with open(path_venv_path_txt, "rt") as fin:
            for line in fin:
                env_has_path_txt = 1
                path_txt = line
            if env_has_path_txt ==0:
                path_txt = ''
    else:
        path_txt = ''

    # ECON_Properties settings
    # use_smpl: StringProperty(name="Use SMPL", default="")
    selected_image: StringProperty(name="Selected Image", default="")
    use_smpl_hand: BoolProperty(name="Use SMPL Hand", default=(True))
    use_smpl_face: BoolProperty(name="Use SMPL Face", default=(False))
    thickness: FloatProperty(name="Thickness", default=0.02)
    k: IntProperty(name="K", default=4)
    hps_type: EnumProperty(name="HPS Type",
                           items=[
            ("pixie", "Pixie", ""),
            ("pymaf", "Pymaf", "")
        ],
        default="pixie")
    texture_src: EnumProperty(name="Texture Source", 
                              items=[
            ("image", "Image", ""),
            ("stable_diffusion", "Stable Diffusion", "")
        ],
        default="image")
    use_ifnet: BoolProperty(name="Use IFNet", default=False)


    str_venv_path: StringProperty(name="Venv Path", description="Place to install/use Venv",default = path_txt)
    str_sd_prompt: StringProperty(name="Prompt", description="Prompt for text2light")
    str_custom_venv_name: StringProperty(name='Name',default=DEFAULT_NAME,update=updt_custom_venv_name)
    bool_custom_venv: BoolProperty(name='Custom venv',default=False,update=updt_bool_custom_venv)
    str_custom_venv_name: StringProperty(name='Name',default=DEFAULT_NAME,update=updt_custom_venv_name)
    bool_custom_venv_name: BoolProperty(name='Custom venv Name',default=False,update=updt_bool_venv_custom_name)
    bool_custom_venv_name_from_list: BoolProperty(name='Custom venv Name from List',default=False,update=updt_bool_venv_custom_name_from_list)
    enum_custom_venv_list : EnumProperty(
        name="Folder",
        description="Select Existing compatible folder.",
        items=folder_venv_callback,
        update=update_venv_name_from_list
        )
    fl_bg_strength: FloatProperty(name='Strength', min=0.0,default=1.0,update=update_bg_strength)
    str_smpl_username: StringProperty(name='user')
    str_smpl_password: StringProperty(name='pass',subtype='PASSWORD')
    bool_erase_zip: BoolProperty(name='Erase Zip',description='Erase zip after unzipping',default=False)
    bool_step1_create_econ_venv: BoolProperty(name='Step 1',default=False)
    bool_step2_downlad_econ: BoolProperty(name='Step 2',default=False)
    bool_step3_install_econ_venv: BoolProperty(name='Step 3',default=False)
    bool_step4_install_compiler: BoolProperty(name='Step 4',default=False)
    bool_step5_finish_econ: BoolProperty(name='Step 5',default=False)
    bool_step6_install_pytorch: BoolProperty(name='Step 6',default=False)
    