# CEB_ECON Unofficial Update

This project contains unofficial updates for the [CEB_ECON](https://carlosedubarreto.gumroad.com/l/CEB_ECON) Blender add-on.

- [ECON](https://github.com/YuliangXiu/ECON) is is designed for "Human digitization from a color image"
- [TEXTure](https://github.com/TEXTurePaper/TEXTurePaper)

---

> Tuned version of ECON & TEXTure for CEB_ECON is available in CEB_ECON ifself and link down below
>
> - [tuned ECON](https://github.com/kwan3854/ECON)
> - [tuned TEXTure](https://github.com/kwan3854/TEXTure_for_ECON)

## Prerequisites

Before using these updates, please ensure to install PyYAML as it is required for the feature allowing config (econ.yaml) modifications. To do this, you need to run the following Python code snippet in the Scripting tab within Blender:

```python
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "PyYAML"])
```

## Release Notes

- **May 26, 2023:**
  - Fix TEXTure install bug
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