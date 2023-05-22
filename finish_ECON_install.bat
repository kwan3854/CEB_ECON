call "C:\ECON_venv\ECON_38_env\Scripts\activate.bat"
set python_include=%1\compilando\Python\include
set python_pc=%1\compilando\Python\PC
set python_libs=%1\compilando\Python\libs
set msvc_include=%1\compilando\MSVC\include
set msvc_atlmfc_include=%1\compilando\MSVC\ATLMFC\include
set win_kit_include_ucrt=%1\compilando\MSVC\windows_kits\include\ucrt
set win_kit_include_shared=%1\compilando\MSVC\windows_kits\include\shared
set win_kit_include_um=%1\compilando\MSVC\windows_kits\include\um
set win_kit_include_winrt=%1\compilando\MSVC\windows_kits\include\winrt
set win_kit_include_cppwinrt=%1\compilando\MSVC\windows_kits\include\cppwinrt
set msvc_atlmfc_lib=%1\compilando\MSVC\ATLMFC\lib\x64
set msvc_lib=%1\compilando\MSVC\lib\x64
set win_kit_ucrt_lib=%1\compilando\windows_kits\lib\ucrt\x64
set win_kit_um_lib=%1\compilando\windows_kits\lib\um\x64
set win_kit_bin=%1\compilando\windows_kits\bin\10.0.19041.0\x64
set todo_msvc_path=%1\compilando\FULL_COMMUNITY_MSVC\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64
set ninja_path=%1\compilando\FULL_COMMUNITY_MSVC\2019\Community\Common7\IDE\CommonExtensions\Microsoft\CMake\Ninja
set INCLUDE=%python_pc%;%python_include%;%win_kit_include_ucrt%;%msvc_include%;%msvc_atlmfc_include%;% win_kit_include_shared%;%win_kit_include_um%;%win_kit_include_winrt%;%win_kit_include_cppwinrt%
set LIB=%python_libs%;%msvc_atlmfc_lib%;%msvc_lib%;%win_kit_ucrt_lib%;%win_kit_um_lib%
set LIBPATH=%msvc_atlmfc_lib%;%msvc_lib%
set PATH=%win_kit_bin%;%todo_msvc_path%;%ninja_path%;%PATH%
cd econ\lib\common\libmesh
python setup.py build_ext --inplace
cd ..
cd libvoxelize
python setup.py build_ext --inplace