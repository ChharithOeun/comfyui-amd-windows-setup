[![CI](https://github.com/ChharithOeun/comfyui-amd-windows-setup/actions/workflows/ci.yml/badge.svg)](https://github.com/ChharithOeun/comfyui-amd-windows-setup/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/chharith)

# ComfyUI AMD Windows Setup

**Install and run ComfyUI on AMD GPU Windows with DirectML — no CUDA needed.**

ComfyUI is a powerful node-based Stable Diffusion workflow engine. This repository automates setup for AMD GPUs on Windows using **DirectML** backend, eliminating the need for NVIDIA-specific tooling or ROCm compilation.

## Quick Start

```bash
git clone https://github.com/ChharithOeun/comfyui-amd-windows-setup.git
cd comfyui-amd-windows-setup

pip install -r requirements.txt

python scripts/install.py
python scripts/launch.py
```

Open your browser to **http://localhost:8188** and start creating.

## What is ComfyUI?

ComfyUI is a node-based interface for Stable Diffusion. Instead of typing prompts in a text box, you build workflows by connecting nodes:

- **Model loaders** → generators → **samplers** → output
- Easily branch pipelines for **inpainting**, **upscaling**, **control networks**
- **Save workflows as JSON**, run them repeatedly with tweaks
- Install **custom nodes** to extend functionality

Perfect for creative professionals, researchers, and automation workflows.

## Features

✅ **DirectML Backend** — Full AMD GPU support on Windows  
✅ **Automatic Installation** — One-command ComfyUI setup  
✅ **Custom Nodes** — Easy install of popular node packs  
✅ **Model Management** — Checkpoints, LoRAs, ControlNets in organized folders  
✅ **Cross-Platform Scripts** — Works on Windows (batch + Python)  
✅ **AMD Optimized** — `--fp32` flag avoids black image issues  
✅ **Fallback to CPU** — If GPU detection fails, runs on CPU  

## Usage

### Launch ComfyUI

```bash
python scripts/launch.py
```

Optionally:
- `--port 8080` — Run on custom port (default: 8188)
- `--no-fp32` — Use fp16 (faster but may cause issues on some AMD GPUs)
- `--cpu` — Force CPU mode

### Install Custom Nodes

```bash
python scripts/install_nodes.py --all
```

Or install a specific node:
```bash
python scripts/install_nodes.py --node ComfyUI-Manager
```

### Verify GPU Setup

```bash
python scripts/verify_gpu.py
```

This checks DirectML support and diagnoses common issues.

### Model Placement

Place models in these folders (created automatically):
- **Checkpoints**: `ComfyUI/models/checkpoints/`
- **LoRAs**: `ComfyUI/models/loras/`
- **ControlNets**: `ComfyUI/models/controlnet/`
- **VAE**: `ComfyUI/models/vae/`
- **Inpainting**: `ComfyUI/models/inpaint/`

## Supported Models

- **Stable Diffusion 1.5** — Original base model
- **Stable Diffusion 2.x** — Higher quality outputs
- **SDXL** — Latest, highest quality (requires more VRAM)
- **ControlNet** — Precise image guidance (pose, depth, canny edge)
- **LoRA** — Lightweight style/concept fine-tuning
- **Inpainting Models** — Mask-based image editing

## Common Issues

### No GPU Detected
Run `python scripts/verify_gpu.py` to diagnose:
- Are AMD drivers installed?
- Is torch-directml installed?
- Try `--cpu` mode as fallback.

### Black/Pink Images (AMD fp16 Bug)
**Solution**: Use `--fp32` flag (enabled by default). If explicitly disabled, add it back:
```bash
python scripts/launch.py  # includes --fp32 by default
```

### Out of Memory
- Start with **Stable Diffusion 1.5** instead of SDXL
- Reduce resolution: `512x512` instead of `768x768`
- Use `--fp16` if your GPU has sufficient VRAM and doesn't show artifacts
- Enable tiling or optimization nodes in ComfyUI UI

## AMD-Specific Notes

**Why `--fp32`?**  
Some AMD GPUs have issues with fp16 (half precision), resulting in black/pink outputs. `--fp32` (full precision) is safer.

**Disable xformers:**  
xformers is NVIDIA-optimized. ComfyUI auto-detects and skips it on DirectML.

**Driver Compatibility:**  
- AMD Radeon drivers (20.50+) required
- Update via AMD Radeon Software or Windows Update

## Part of AMD Windows AI Ecosystem

This repo is one of several tools for running modern AI on AMD Windows hardware:

- **[amd-windows-toolkit](https://github.com/ChharithOeun/amd-windows-toolkit)** — Central hub for AMD GPU setup, LLM runners, environment validation
- **comfyui-amd-windows-setup** ← you are here  
- **Other models & runners coming soon**

Check out the toolkit for unified AMD GPU discovery, PyTorch DirectML validation, and more.

## Support

Found a bug or have a feature request? Open an [Issue](https://github.com/ChharithOeun/comfyui-amd-windows-setup/issues).

Want to contribute? See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License — see [LICENSE](LICENSE)

---

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/chharith)

If this project saved you hours of setup, consider buying me a coffee!
