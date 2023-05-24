@set "VIRTUAL_ENV=C:\ECON_venv\ECON_38_env"

@if defined _OLD_VIRTUAL_PROMPT (
    @set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
) else (
    @if not defined PROMPT (
        @set "PROMPT=$P$G"
    )
    @if not defined VIRTUAL_ENV_DISABLE_PROMPT (
        @set "_OLD_VIRTUAL_PROMPT=%PROMPT%"
    )
)
@if not defined VIRTUAL_ENV_DISABLE_PROMPT (
    @if "" NEQ "" (
        @set "PROMPT=() %PROMPT%"
    ) else (
        @for %%d in ("%VIRTUAL_ENV%") do @set "PROMPT=(%%~nxd) %PROMPT%"
    )
)

@REM Don't use () to avoid problems with them in %PATH%
@if defined _OLD_VIRTUAL_PYTHONHOME @goto ENDIFVHOME
    @set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"
:ENDIFVHOME

@set PYTHONHOME=

@REM if defined _OLD_VIRTUAL_PATH (
@if not defined _OLD_VIRTUAL_PATH @goto ENDIFVPATH1
    @set "PATH=%_OLD_VIRTUAL_PATH%"
:ENDIFVPATH1
@REM ) else (
@if defined _OLD_VIRTUAL_PATH @goto ENDIFVPATH2
    @set "_OLD_VIRTUAL_PATH=%PATH%"
:ENDIFVPATH2

@set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

                    cd "C:\Users\LEE\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\CEB_ECON"
                    echo --------------------------------------------------
                    echo Downloading and unzipping TEXTure...
                    python -m urllib.request https://github.com/YuliangXiu/TEXTure/archive/022761263660c5dece411766eefe7735eb2cfd6a.zip C:\Users\LEE\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\CEB_ECON\TEXTure_github.zip
                    python -m zipfile -e C:\Users\LEE\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\CEB_ECON\TEXTure_github.zip C:\Users\LEE\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\CEB_ECON
                    echo Renaming and removing the zip file...
                    python -m os.rename C:\Users\LEE\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\CEB_ECON\TEXTure-022761263660c5dece411766eefe7735eb2cfd6a C:\Users\LEE\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\CEB_ECON\ECON\TEXTure
                    python -m os.remove C:\Users\LEE\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\CEB_ECON\TEXTure_github.zip
                    echo --------------------------------------------------
                    echo Installing diffusers...
                    pip install --upgrade diffusers[torch]
                    echo --------------------------------------------------
                    echo Installing TEXTure dependencies...
                    python -mpip install -r "C:\Users\LEE\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\CEB_ECON\ECON\TEXTure\requirements.txt"
                    python -mpip install kaolin==0.13.0 -f https://nvidia-kaolin.s3.us-east-2.amazonaws.com/torch-1.12.1_cu116.html
                    echo --------------------------------------------------
                    echo YOU CAN CLOSE THIS WINDOW NOW
                    echo --------------------------------------------------
                