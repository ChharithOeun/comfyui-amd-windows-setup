# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2024-04-19

### Added
- Initial release of ComfyUI AMD Windows Setup
- Automated ComfyUI installer with DirectML backend (`scripts/install.py`)
- ComfyUI launcher with AMD-optimized settings (`scripts/launch.py`)
- GPU verification tool (`scripts/verify_gpu.py`)
- Custom node installer with popular node pack support (`scripts/install_nodes.py`)
- Interactive menu batch script (`run.bat`)
- Comprehensive installation guide (`INSTALL.md`)
- Contributing guidelines (`CONTRIBUTING.md`)
- MIT License
- GitHub CI/CD workflows (Python syntax validation on Windows/macOS/Linux × Python 3.10/3.11/3.12)
- GitHub issue templates (bug report, feature request)
- Badges in README (CI, License, Python version, Buy Me A Coffee)

### Features
- DirectML backend for AMD GPU support on Windows
- Automatic ComfyUI repository cloning and setup
- fp32 precision by default (AMD GPU stability)
- Port customization (default: 8188)
- Popular custom node registry: ComfyUI-Manager, ComfyUI-Impact-Pack, was-node-suite-comfyui, controlnet-aux
- GPU detection and diagnostic reporting
- Cross-platform Python scripts (tested on Windows)

### Documentation
- README with quick start, features, usage examples
- INSTALL.md with detailed step-by-step setup guide
- CONTRIBUTING.md for community contributions
- CHANGELOG.md for release tracking

### Known Issues
- DirectML device detection may fail on older AMD drivers (workaround: update to latest Radeon driver)
- Some SDXL models require 8+ GB VRAM
- ComfyUI itself is a separate large repository (git-cloned, not included)

---

[Unreleased]: https://github.com/ChharithOeun/comfyui-amd-windows-setup/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/ChharithOeun/comfyui-amd-windows-setup/releases/tag/v1.0.0
