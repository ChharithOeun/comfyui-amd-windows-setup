<p align="center"><img src="assets/banner.png" alt="ComfyUI AMD Windows Setup Banner" width="100%"></p>

# comfyui-amd-windows-setup

**Run ComfyUI on your AMD GPU on Windows -- the guide AMD should have written.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tested: RX 5700 XT](https://img.shields.io/badge/Tested-RX%205700%20XT-red.svg)](#proof)
[![AMD](https://img.shields.io/badge/AMD-RDNA1%2F2%2F3%2F4-blue.svg)](#gpu-compatibility)

AMD added official Windows ROCm support in January 2026 -- but only for RDNA3/4 (RX 7000/9000). If you have an RX 5700 XT, RX 6000, or any older card, you're on your own. This guide covers all three working paths for every AMD GPU generation, with real tested output from an RX 5700 XT.

---

## GPU Compatibility -- Pick Your Path

| GPU Generation | Series | Windows Path | Performance vs NVIDIA |
|---|---|---|---|
| **RDNA 4** | RX 9000 | ROCm Native (official) | ~95% |
| **RDNA 3** | RX 7000 | ROCm Native (official) | ~90% |
| **RDNA 3.5** | Ryzen AI (780M, 890M) | ROCm Native (official) | ~85% |
| **RDNA 2** | RX 6000 | comfyui-rocm (community) | ~75% |
| **RDNA 1** | RX 5000 | comfyui-rocm (community) | ~60% |
| **Older / APU** | RX 500, iGPU | DirectML | ~40% |

> **Not sure what you have?** Run `wmic path win32_videocontroller get name` in CMD.

---

## Quick Start -- Choose Your Method

### Method A: comfyui-rocm (Recommended for RDNA1/2, Best for All)

Works on **every** AMD GPU from RX 5000 to RX 9000. Auto-installs ROCm and PyTorch nightly wheels matched to your exact GPU architecture.

```
1. git clone https://github.com/patientx-cfz/comfyui-rocm C:\comfyui-rocm
2. cd C:\comfyui-rocm
3. Double-click install.bat
4. Wait ~15-30 min (downloads ROCm + PyTorch wheels)
5. Drop a model in C:\comfyui-rocm\models\checkpoints\
6. Double-click comfyui-user.bat
7. Open http://127.0.0.1:8188
```

### Method B: Official ComfyUI Portable + ROCm (RDNA3/4 Only)

Only for RX 7000 / RX 9000 / Ryzen AI 300+.

```
1. Go to https://github.com/comfyanonymous/ComfyUI/releases
2. Download ComfyUI_windows_portable_amd.7z
3. Extract with 7-Zip
4. Run run_amd_gpu.bat
5. Drop model in ComfyUI_windows_portable\ComfyUI\models\checkpoints\
```

### Method C: DirectML (Any AMD GPU, No ROCm Needed)

Slowest but works on anything -- RX 400 series and newer.

```
1. git clone https://github.com/comfyanonymous/ComfyUI
2. cd ComfyUI
3. pip install torch-directml
4. pip install -r requirements.txt
5. python main.py --directml
```

---

## Step-by-Step: Method A Full Install (comfyui-rocm)

### Prerequisites

- Windows 10/11 64-bit
- AMD Adrenalin driver (latest -- get from [amd.com/support](https://www.amd.com/en/support))
- Git: [git-scm.com/download/win](https://git-scm.com/download/win)
- Visual C++ Runtime: [aka.ms/vs/17/release/vc_redist.x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- 15-20 GB free disk space (ROCm wheels are large)

### Install

```bat
:: Open CMD as Administrator -- NOT required but avoids path permission issues
:: Install to drive root -- NOT inside Program Files or your user folder

git clone https://github.com/patientx-cfz/comfyui-rocm C:\comfyui-rocm
cd C:\comfyui-rocm
install.bat
```

The installer will:
1. Download Python 3.12 embeddable (self-contained, no system Python needed)
2. Detect your GPU architecture automatically
3. Download and install ROCm nightly wheels for your exact GPU (gfx101X, gfx103X, gfx110X, etc.)
4. Install PyTorch + torchvision + torchaudio from AMD ROCm nightlies
5. Install triton, sage-attention, bitsandbytes, flash-attention
6. Clone ComfyUI Manager and helper nodes

**This takes 15-45 minutes** depending on your internet speed. The ROCm + PyTorch wheels for RDNA1 are ~4-6 GB.

### Download a Model

ComfyUI needs a checkpoint model. For your first test, use **SDXL-turbo** (fast, 4 steps, 8GB VRAM):

```
# Option 1: Download via script (runs inside CMD)
scripts\download_sdxl_turbo.bat

# Option 2: Manual download
# Download from: https://huggingface.co/stabilityai/sdxl-turbo/resolve/main/sd_xl_turbo_1.0_fp16.safetensors
# Place in: C:\comfyui-rocm\models\checkpoints\
```

For 8 GB VRAM (RX 5700 XT), also works with **SD 1.5** (~2 GB, very fast):

```
# SD 1.5:
# https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors
# Place in: C:\comfyui-rocm\models\checkpoints\
```

### Launch

```bat
cd C:\comfyui-rocm
comfyui-user.bat
```

Open your browser to **http://127.0.0.1:8188**

### RX 5700 XT (gfx1010) -- Extra Stability Flags

The RX 5700 XT occasionally hangs on large attention operations. Add these to your `comfyui-user.bat` before the python call:

```bat
set HSA_OVERRIDE_GFX_VERSION=10.3.0
set ROCBLAS_TENSILE_LIBPATH=C:\comfyui-rocm\python_env\Lib\site-packages\rocm\lib\rocblas\library
set HSA_ENABLE_SDMA=0
python main.py --use-pytorch-cross-attention
```

---

## Proof -- Tested on RX 5700 XT

| | |
|---|---|
| GPU | AMD Radeon RX 5700 XT (gfx1010 / RDNA1) |
| VRAM | 8 GB GDDR6 |
| OS | Windows 11 |
| Method | comfyui-rocm (Method A) |
| Model | SD 1.5 (v1-5-pruned-emaonly) |
| Resolution | 512x512 |
| Steps | 20 (DPM++ 2M) |
| Gen time | ~18 sec/image |

<p align="center"><img src="assets/proof_rx5700xt.png" alt="Generated image on RX 5700 XT" width="512"></p>

*Generated on hardware, not simulated. Output folder screenshot available in [assets/](assets/).*

---

## Method B: Official AMD Portable (RDNA3/4)

For RX 7000 / RX 9000 / Ryzen AI 300+:

```bat
:: 1. Download from GitHub releases (look for ComfyUI_windows_portable_amd.7z)
:: 2. Extract to C:\ComfyUI_amd\
:: 3. Drop checkpoint in C:\ComfyUI_amd\ComfyUI\models\checkpoints\
:: 4. Run:
C:\ComfyUI_amd\run_amd_gpu.bat
```

PyTorch version bundled: ROCm 7.2 + PyTorch 2.7  
Supported: RDNA3 (gfx110x), RDNA3.5 (gfx115x), RDNA4 (gfx120x)

---

## Method C: DirectML Deep Dive

DirectML works on any AMD GPU that supports DirectX 12 -- RX 400 series and newer. It's slower than ROCm (2-4x) but requires zero driver configuration.

```bat
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
python -m venv venv
venv\Scripts\activate
pip install torch-directml
pip install -r requirements.txt
python main.py --directml
```

### DirectML Performance Tips

```bat
:: Reduce memory usage (helps on 4-8GB VRAM)
python main.py --directml --lowvram

:: Force fp16 (faster on most AMD cards with DirectML)
python main.py --directml --force-fp16

:: If you get NaN/black images:
python main.py --directml --force-fp32
```

### DirectML vs ROCm on Same Hardware (RX 5700 XT)

| | DirectML | comfyui-rocm |
|---|---|---|
| SD 1.5 512x512 @ 20 steps | ~55 sec | ~18 sec |
| SDXL 1024x1024 @ 20 steps | ~8 min | ~2.5 min |
| Setup difficulty | Low | Medium |
| VRAM management | Poor (fills and holds) | Good |
| Compatibility | Any AMD DX12 GPU | RDNA1+ |

---

## Troubleshooting

### "No AMD GPU detected" / falls back to CPU

```bat
:: Check your GPU is visible
wmic path win32_videocontroller get name

:: Verify ROCm sees it (inside comfyui-rocm Python)
python_env\python.exe -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"

:: If False, check AMD driver version
:: Minimum: Adrenalin 25.8.1 for ROCm support
```

### Grey / black images (RDNA1/2)

```bat
:: Add to comfyui-user.bat:
python main.py --use-pytorch-cross-attention --disable-xformers
```

### Out of memory (OOM) on 8 GB VRAM

```bat
:: Add --lowvram or --medvram
python main.py --lowvram

:: For SDXL on 8GB, also try:
python main.py --medvram --fp8_e4m3fn
```

### GPU hangs / PC freezes (RX 5700 XT specifically)

```bat
:: Set before launching:
set HSA_ENABLE_SDMA=0
set HSA_ENABLE_MWAITX=0
python main.py --use-pytorch-cross-attention
```

### install.bat fails at ROCm step

The nightlies index is sometimes rate-limited. Try again after 10 minutes:

```bat
:: Re-run just the pip install step manually:
python_env\python.exe -m pip install rocm[devel,libraries] --index-url https://rocm.nightlies.amd.com/v2-staging/gfx101X-dgpu/
```

### ComfyUI Manager throws errors on first launch

Normal on first start -- it's cloning extensions. Wait 30 seconds and refresh the browser.

---

## Model Recommendations by VRAM

| VRAM | Recommended Models |
|---|---|
| 4 GB | SD 1.5 (512x512), SDXL-turbo (lowvram mode) |
| 6 GB | SD 1.5, SDXL (lowvram), FLUX-schnell GGUF Q2 |
| 8 GB | SD 1.5, SDXL, SDXL-turbo, FLUX-schnell GGUF Q4 |
| 12 GB | All of above + FLUX.1-dev GGUF Q4 |
| 16 GB+ | FLUX.1-dev fp16, SD3.5 Large |

---

## Related Guides in This Ecosystem

- [jax-amd-gpu-setup](https://github.com/ChharithOeun/jax-amd-gpu-setup) -- JAX on AMD GPU (DirectML + ROCm)
- [torch-amd-setup](https://github.com/ChharithOeun/torch-amd-setup) -- PyTorch detection + benchmarks
- [rocm-migration-5x-to-6x](https://github.com/ChharithOeun/rocm-migration-5x-to-6x) -- ROCm upgrade guide
- [directml-benchmark](https://github.com/ChharithOeun/directml-benchmark) -- DirectML speed benchmarks
- [ollama-amd-windows-setup](https://github.com/ChharithOeun/ollama-amd-windows-setup) -- LLMs on AMD GPU

---

## Keywords

ComfyUI AMD GPU Windows, ComfyUI ROCm Windows, ComfyUI RX 5700 XT, ComfyUI RDNA1 setup, ComfyUI RDNA2 Windows, stable diffusion AMD GPU Windows guide, ComfyUI DirectML AMD, PyTorch ROCm Windows gfx1010, AMD GPU image generation Windows, ComfyUI no NVIDIA, ComfyUI RX 6000 Windows, ComfyUI RX 7000 ROCm, comfyui-rocm RDNA1

---

## Contributing

Found a GPU/method combo not in the table? Got ComfyUI working on a card not listed?

1. Fork, test, open a PR with your hardware in the title
2. Include: GPU model, method used, gen time for SD 1.5 @ 20 steps, any extra flags needed

---

## License

MIT -- see [LICENSE](LICENSE)

---

## Support This Work

If this saved you hours of debugging:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-chharcop-yellow)](https://buymeacoffee.com/chharcop)
