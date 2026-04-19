# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [1.0.0] - 2026-04-19

### Added

- README.md: Full three-path guide (comfyui-rocm / Official AMD Portable / DirectML)
- GPU compatibility table covering RDNA1 through RDNA4
- Proof section: tested on RX 5700 XT (gfx1010 / RDNA1)
- Troubleshooting section: grey images, OOM, GPU hangs, install failures
- Model recommendations by VRAM (4GB through 16GB+)
- DirectML vs ROCm performance comparison table
- RX 5700 XT stability flags (HSA_ENABLE_SDMA=0, pytorch-cross-attention)
- scripts/download_sdxl_turbo.bat: one-click model downloader
- scripts/download_sd15.bat: one-click SD 1.5 downloader
- .github/workflows/changelog.yml: auto-update changelog on push

### Covers

- RDNA1 (RX 5000 series) through RDNA4 (RX 9000 series)
- Windows 10 and Windows 11
- comfyui-rocm (community ROCm), Official AMD Portable, DirectML
- Proof-tested on AMD Radeon RX 5700 XT

[1.0.0]: https://github.com/ChharithOeun/comfyui-amd-windows-setup/releases/tag/v1.0.0
