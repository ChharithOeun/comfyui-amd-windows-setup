# ComfyUI AMD Windows Installation Guide

Complete step-by-step instructions for setting up ComfyUI on AMD GPU Windows.

## Prerequisites

### 1. Install Git

Download and install from [git-scm.com](https://git-scm.com/download/win).

Verify installation:
```bash
git --version
```

### 2. Install Python 3.10+

Download from [python.org](https://www.python.org/downloads/).

**Important**: During installation, check "Add Python to PATH".

Verify installation:
```bash
python --version
python -m pip --version
```

### 3. Update AMD Radeon Drivers

1. Go to [AMD's official driver page](https://www.amd.com/en/support)
2. Select your GPU model and operating system (Windows)
3. Download and install the latest Radeon driver

After driver installation, restart your computer.

Verify GPU is recognized:
```bash
dxdiag  # Look for your GPU under Display tab
```

## Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/ChharithOeun/comfyui-amd-windows-setup.git
cd comfyui-amd-windows-setup
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `torch-directml`: NVIDIA PyTorch redirected to AMD DirectML backend

### Step 3: Automated ComfyUI Installation

```bash
python scripts/install.py
```

This will:
1. ✓ Check Python version
2. ✓ Clone ComfyUI repository
3. ✓ Install torch, torchvision, and other dependencies
4. ✓ Create `ComfyUI/launch_amd.bat` launcher script

**Optional flags**:
- `--skip-clone` — if ComfyUI already cloned
- `--port 8080` — custom port (default: 8188)
- `--no-fp32` — use fp16 instead (not recommended for AMD)

### Step 4: Verify GPU Setup

```bash
python scripts/verify_gpu.py
```

Expected output:
```
✓ torch-directml is installed
✓ DirectML device detected (count: 1)
✓ Tensor operation successful on DirectML device
✓ ComfyUI installed at: C:\path\ComfyUI
```

If DirectML device is not detected:
1. Verify AMD drivers are installed: `dxdiag` → Display tab
2. Reinstall torch-directml: `pip install --upgrade torch-directml`
3. Restart your computer

### Step 5: Launch ComfyUI

```bash
python scripts/launch.py
```

Or use the batch file:
```bash
ComfyUI/launch_amd.bat
```

You should see:
```
ℹ DirectML with fp32 (AMD optimized)
Launching ComfyUI on port 8188...
Open: http://localhost:8188
```

### Step 6: Open ComfyUI Web UI

In your browser, go to: **http://localhost:8188**

You should see the ComfyUI node editor interface.

## Model Installation

### Download Models

1. Go to [Civitai](https://civitai.com/) or [Hugging Face](https://huggingface.co/)
2. Search for:
   - **Checkpoints** (`.safetensors` files): "Stable Diffusion 1.5", "SDXL", etc.
   - **LoRA files** (`.safetensors`): Style LoRAs, concept LoRAs
   - **ControlNets** (`.safetensors`): Pose, depth, canny edge, etc.

### Place Models in Correct Folders

After downloading, place files in these directories (created automatically):

```
ComfyUI/models/
  ├── checkpoints/          # Main diffusion models (SD 1.5, SDXL, etc.)
  ├── loras/                # LoRA fine-tuning files
  ├── controlnet/           # ControlNet models
  ├── vae/                  # VAE models (optional, included in checkpoints)
  └── inpaint/              # Inpainting models (optional)
```

**Example**:
- Download `sd-v1-5.safetensors` → Place in `ComfyUI/models/checkpoints/`
- Download `my-style.safetensors` (LoRA) → Place in `ComfyUI/models/loras/`

Models appear automatically in the ComfyUI UI after restart.

## AMD-Specific Settings

### Why `--fp32`?

Some AMD GPUs produce **black/pink images** when using **fp16 (half precision)** due to precision limitations.

**Solution**: Use `--fp32` (full precision) — enabled by default.

If you explicitly disabled it and get artifacts:
```bash
python scripts/launch.py  # Automatically includes --fp32
```

### Memory Optimization

If you run out of VRAM:

1. **Reduce image resolution** in the KSampler node:
   - 512×512 instead of 768×768
   - 768×768 instead of 1024×1024

2. **Use tiling**:
   - In ComfyUI UI, search for "Latent Tiling" or "Tile" nodes

3. **Start with smaller models**:
   - Stable Diffusion 1.5 (uses ~2 GB VRAM)
   - Then upgrade to SDXL if your GPU has 8+ GB

4. **Disable unused extensions**:
   - Disable xformers (auto-skipped on DirectML anyway)
   - Remove unused custom nodes

### Disabling xformers

ComfyUI automatically detects DirectML and skips xformers. No action needed.

## Custom Nodes

Install popular node packs:

```bash
python scripts/install_nodes.py --all
```

This installs:
- **ComfyUI-Manager** — Browse and install nodes via UI
- **ComfyUI-Impact-Pack** — Face detection, upscaling
- **was-node-suite-comfyui** — Image utilities
- **controlnet-aux** — ControlNet preprocessors

**Or install specific nodes**:
```bash
python scripts/install_nodes.py --node ComfyUI-Manager
```

After installation, restart ComfyUI to see new nodes.

## Workflow Example: Text-to-Image

1. In ComfyUI, click **"Load Default"** (if available)
2. Or manually build:
   - **CheckpointLoader** → Load your `.safetensors` checkpoint
   - **CLIPTextEncode** → Positive prompt: "a dog wearing sunglasses, colorful"
   - **CLIPTextEncode** → Negative prompt: "blurry, low quality"
   - **KSampler** → Connect all above, set steps to 20
   - **VAEDecode** → Connect sampler output
   - **SaveImage** → Connect VAE output

3. Click **Queue Prompt**
4. Output appears in `ComfyUI/output/` and in UI

## Troubleshooting

### ComfyUI Won't Start

**Error**: `No module named 'torch_directml'`

**Fix**:
```bash
pip install torch-directml
```

### Black/Pink Image Output

**Cause**: fp16 precision issue on AMD

**Fix**: Ensure `--fp32` is enabled (default):
```bash
python scripts/launch.py
```

### Slow Generation (Using CPU Instead of GPU)

**Verify GPU is used**:
```bash
python scripts/verify_gpu.py
```

If no DirectML device:
1. Update AMD drivers
2. Reinstall torch-directml: `pip install --upgrade torch-directml`
3. Restart computer

### Port Already in Use

**Error**: `Port 8188 already in use`

**Fix**: Use a different port:
```bash
python scripts/launch.py --port 8080
```

### Out of Memory

See [Memory Optimization](#memory-optimization) above.

## Supported Models

| Model | VRAM | Quality | Speed |
|-------|------|---------|-------|
| SD 1.5 | 2 GB | Good | Fast |
| SD 2.1 | 4 GB | Very Good | Medium |
| SDXL 1.0 | 8+ GB | Excellent | Slow |
| ControlNet | +1 GB | — | Slight slowdown |
| LoRA (each) | Minimal | Style/Concept | Negligible |

## Next Steps

1. ✓ Installation complete
2. Launch ComfyUI: `python scripts/launch.py`
3. Install models from Civitai / Hugging Face
4. Explore custom nodes: `python scripts/install_nodes.py --all`
5. Build workflows by connecting nodes

## Support

- **Issue?** Open a [GitHub Issue](https://github.com/ChharithOeun/comfyui-amd-windows-setup/issues)
- **Contributing?** See [CONTRIBUTING.md](CONTRIBUTING.md)
- **Questions?** Check [README.md](README.md)

---

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/chharith)
