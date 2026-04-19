#!/usr/bin/env python3
"""
Verify AMD GPU Setup for ComfyUI

Checks DirectML device detection and ComfyUI installation.
Provides diagnostic info and fix suggestions.

Usage:
    python scripts/verify_gpu.py
"""

import sys
from pathlib import Path

try:
    import torch
except ImportError:
    print("ERROR: torch not installed")
    print("Run: pip install torch-directml")
    sys.exit(1)


def check_directml_available():
    """Check if torch-directml is available."""
    try:
        import torch_directml
        return True
    except ImportError:
        return False


def check_device_count():
    """Get DirectML device count."""
    if not check_directml_available():
        return None

    import torch_directml

    try:
        device = torch_directml.device()
        return 1  # torch-directml uses single unified device
    except Exception:
        return 0


def test_tensor_operation():
    """Test tensor operation on DirectML device."""
    if not check_directml_available():
        return False, "torch-directml not available"

    try:
        import torch_directml

        device = torch_directml.device()
        tensor = torch.randn(2, 3, device=device)
        result = tensor @ tensor.T

        return True, f"Tensor shape: {result.shape}, dtype: {result.dtype}"
    except Exception as e:
        return False, str(e)


def check_comfyui_installed():
    """Verify ComfyUI directory exists."""
    comfyui_path = Path("ComfyUI")
    main_py = comfyui_path / "main.py"

    if comfyui_path.exists() and main_py.exists():
        return True, str(comfyui_path.resolve())
    return False, None


def check_pytorch_version():
    """Get PyTorch version."""
    return torch.__version__


def print_summary(device_count, tensor_ok, comfyui_ok, comfyui_path, pytorch_version):
    """Print diagnostic summary."""
    print()
    print("=" * 60)
    print("AMD GPU Setup Summary")
    print("=" * 60)
    print()

    print(f"PyTorch version: {pytorch_version}")
    print()

    if check_directml_available():
        print("✓ torch-directml is installed")
    else:
        print("✗ torch-directml NOT found")
        print("  Fix: pip install torch-directml")
        print()

    if device_count is not None and device_count > 0:
        print(f"✓ DirectML device detected (count: {device_count})")
    elif device_count is not None:
        print("✗ DirectML device NOT detected")
        print("  Possible causes:")
        print("    - AMD drivers not installed (update Radeon drivers)")
        print("    - GPU not supported (requires RDNA or older with proper driver)")
        print("    - torch-directml version mismatch")
        print()
        print("  Fix:")
        print("    1. Update AMD Radeon drivers to latest version")
        print("    2. Reinstall torch-directml: pip install --upgrade torch-directml")
        print()
    else:
        print("? DirectML availability unclear")
        print()

    if tensor_ok:
        print("✓ Tensor operation successful on DirectML device")
        print(f"  {tensor_ok}")
    else:
        print("✗ Tensor operation FAILED")
        print(f"  Error: {tensor_ok}")
        print()

    if comfyui_ok:
        print(f"✓ ComfyUI installed at: {comfyui_path}")
    else:
        print("✗ ComfyUI NOT found at ./ComfyUI/")
        print("  Fix: python scripts/install.py")
        print()

    print()
    print("=" * 60)

    if device_count and tensor_ok and comfyui_ok:
        print("✓ All systems ready! Run: python scripts/launch.py")
    else:
        print("⚠ Issues detected. See suggestions above.")

    print("=" * 60)
    print()


def main():
    print("Verifying AMD GPU setup for ComfyUI...")
    print()

    device_count = check_device_count()
    tensor_ok, tensor_msg = test_tensor_operation()
    comfyui_ok, comfyui_path = check_comfyui_installed()
    pytorch_version = check_pytorch_version()

    print_summary(device_count, tensor_msg, comfyui_ok, comfyui_path, pytorch_version)


if __name__ == "__main__":
    main()
