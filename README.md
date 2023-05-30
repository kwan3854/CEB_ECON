# CEB_ECON Unofficial Update

This project contains unofficial updates for the [CEB_ECON](https://carlosedubarreto.gumroad.com/l/CEB_ECON) Blender add-on.

- [ECON](https://github.com/YuliangXiu/ECON) is is designed for "Human digitization from a color image"
- [TEXTure](https://github.com/TEXTurePaper/TEXTurePaper)

---

> Tuned version of ECON & TEXTure for CEB_ECON is available in CEB_ECON ifself and link down below
>
> - ~~[tuned ECON](https://github.com/kwan3854/ECON)~~ Merged to official ECON
> - [tuned TEXTure](https://github.com/kwan3854/TEXTure_for_ECON)

## Installation Guide

### Download

1. Click on the green `<> Code` button and select `Download ZIP`.

   - This will download the `CEB_ECON-main.zip` file.

2. Visit the original [CEB_ECON](https://carlosedubarreto.gumroad.com/l/CEB_ECON) page, name your fair price, and click on the 'purchase' button.

   - *If this project has been helpful to you, please consider supporting [Carlos Barreto](https://twitter.com/carlosedubarret) and CEB Studios on their [Patreon](https://www.patreon.com/cebstudios) page.*

3. **[RECOMMENDED]** Download `CUDA 11.6` and `vs_BuildTools.exe`.

   > [NOT RECOMMENDED] Instead of installing `CUDA 11.6` and `VS BuildTools`, you can download `JIT_Compiler_PY38_CUDAv11.6.7z` from [this link](https://carlosedubarreto.gumroad.com/l/dependency/2jhtxqo) and install it from Blender.
   >
   > - *You can skip this step if you have already installed CUDA 11.6 and Visual Studio 2019.*

4. Obtain Hugging Face Tokens

   1. Register for a Hugging Face account and log in.
   2. Navigate to the https://huggingface.co/settings/tokens page.
   3. Create a new token.
      1. Click on the `New token` button.
      2. Name it (e.g., ECON).
      3. Set the role to 'read'.
      4. Generate the token.
   4. Copy the token, paste it into `notepad`, and save the token text as a .txt file. Remove the .txt extension and name this file `TOKEN`.

### Installation

1. **`vs_BuildTools.exe`**

   1. Open `vs_BuildTools.exe`.
   2. Install the C++ build tools.

2. **`CUDA 11.6`**

   - Install `CUDA 11.6`.

3. Run Blender **as an administrator**.

4. Navigate to the `Scripting` tab in Blender and copy-paste this code:

   ```python
   import subprocess
   import sys
   subprocess.check_call([sys.executable, "-m", "pip", "install", "ruamel.yaml"])
   ```
   
5. Press the `Enter` key and ensure that it returns 0:

   ```python
   >>> import subprocess
   >>> import sys
   >>> subprocess.check_call([sys.executable, "-m", "pip", "install", "ruamel.yaml"])
   0
   ```
   
6. Navigate to `Edit` -> `Preferences` -> `Add-ons`. Click on the `Install` button and select the `CEB_ECON-main.zip` file. Then, click on `Install Add-on`.

7. Enable the CEB_ECON add-on by clicking on `General: CEB ECON`. Close the Preferences window.

8. Navigate to `Window` -> `Toggle System Console` and keep this window open for reference.

   - From this point forward, keep an eye on this window for any potential errors as you proceed with the installation process.

9. Open the `ECON Install` tab in Blender.

   - Click on the arrow button on the right side.
   - Click on `ECON Install` to open the installation tab.

10. Click on `Venv and Installs` to open the tab.

11. Click on `Path` and choose the directory in which to install the virtual environment (venv).

    - For example, C:\ECON_VENV

12. Click on `Create ECON Venv` and wait for the process to complete.

13. Click on `Download ECON` and wait for the download to complete.

14. Click on `Finish ECON Install` and wait for the installation to finish.

15. Click on `Down&Install Pytorch_3D` and wait for the process to complete.

16. Click on `Download TEXTure` and wait for the download to complete.

17. Click on the `Register` button, then go to `Login` -> `Register` to register.

18. Log in.

19. Click on the `Register on all` button from the Blender add-on.

20. Register *all projects* by clicking on the `Register now` buttons.

21. Go back to Blender, type your ID and password, then click `Download`.

    - **This may take some time.** Wait until the process is finished. (if you see `Out: pymafx_data.zip` on the console window, it means the process is finished.)
    - This add-on does not collect your ID and password data.

22. If desired, you can delete downloaded zip files by checking `Erase Zip` and clicking on the `Download` button once more.

23. Copy the `TOKEN` file to `C:\Users\{USER NAME}\AppData\Roaming\Blender Foundation\Blender\{BLENDER VERSION}\scripts\addons\CEB_ECON-main\ECON\TEXTure\` .

### Test Run

*Blender requires administrative privileges for the first run.*

1. Navigate to the `ECON Generate Models` tab on the right side to generate 3D models.

2. [Optional] You can change the `ECON Settings`

    and click on `Save Configuration`.

   - Refer to this [page](https://github.com/YuliangXiu/ECON/blob/master/docs/tricks.md) to understand how each option affects the output.

3. Import a full-body image by clicking on `Import Image`.

4. Click on `Generate 3D Model` to generate a 3D model from the provided image.

   - Per vertex color is included. You can check it by navigating to `Material Properties` -> `New` -> `Base Color` (click circle button) -> `Input` -> `Color Attribute`.

5. Click on `Generate Animatable 3D Model` to generate a model in *A pose* with a *UV mapped texture file*.

6. To generate a backside texture, write a prompt that describes your image and click on Generate texture.

   - For example, *A man wearing a black T-shirt, black jeans, and black shoes.*

7. After the first run, Blender no longer requires administrative privileges.

## Release Notes

- **May 26, 2023:**
  - Fix TEXTure install bug
  - Fix IFNet option
- **May 25, 2023:**
  - Fix imperfect texturing (TEXTure)

- **May 24, 2023:**
  - Updated the TEXTure Feature
  - Updated the Avatarizer Feature
  - UI Improvements

- **May 23, 2023:**
  - Updated the "Download ECON" button to fetch the newer version of ECON, moving from the Jan 09 version to the May 14 version.
  - Enabled config (econ.yaml) modifications directly from the add-on. For usage instructions, refer to the [tricks.md](https://github.com/YuliangXiu/ECON/blob/master/docs/tricks.md). Please note there is a current issue with 'use_ifnet' that needs fixing.

## Upcoming Updates

### For the [Plugin](CEB_ECON)

- Integration with Mixamo.
- ~~Integration with the TEXTure feature is underway, which will include both the installation and usage aspects.~~ (done)

### For [ECON](https://github.com/kwan3854/ECON)

- ~~Working to resolve the xatlas UV mapping issue that causes black seams.~~ (done)
- ~~Improvement of the Texture feature.~~ (done)
- Plans to enable Unity integration are in the pipeline.
- ~~The 'use_ifnet' bug fix is currently being worked on.~~ (done)
- ~~[Directory bug on windows](https://github.com/YuliangXiu/ECON/issues/8)~~ (temp fix on CEB ECON)

##  Tested Environment

The plugin has been tested and validated under the following hardware and software configurations:

- OS: Windows 11 (Please note, only Windows OS is currently supported)
- CPU: Intel i7 13700K
- GPU: NVIDIA RTX 4080 with 16GB VRAM
- RAM: 32GB

performance may vary under different hardware configurations
