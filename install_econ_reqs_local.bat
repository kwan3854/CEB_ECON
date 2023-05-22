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

rem %1 - drive env
rem %2 - path to venv (wihtout drive)
rem %3 - env_folder
C:
cd\Users\LEE\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\addons\CEB_ECON
cd
echo --------------------------------------------------
python -mpip install -r requirements.txt
python -mpip install src\rembg-0+unknown-py3-none-any.whl
python -mpip install src\voxelize_cuda-0.0.0-cp38-cp38-win_amd64.whl
echo --------------------------------------------------------------
echo YOU CAN CLOSE THIS WINDOW NOW
echo --------------------------------------------------------------