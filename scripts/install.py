#!/usr/bin/env python3
"""
ComfyUI AMD Windows Installer

Automates ComfyUI setup for AMD GPUs using DirectML backend.

Usage:
    python scripts/install.py                    # Default: clone ComfyUI, install DirectML
    python scripts/install.py --skip-clone       # Skip cloning (already installed)
    python scripts/install.py --port 8080        # Use custom port
    python scripts/install.py --fp32             # Force fp32 (default for AMD)
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def check_python():
    """Verify Python 3.10+ is available."""
    if sys.version_info < (3, 10):
        print(f"ERROR: Python 3.10+ required. You have {sys.version_info.major}.{sys.version_info.minor}")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")


def check_git():
    """Verify git is installed."""
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        print("✓ Git found")
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("ERROR: Git not found. Install from https://git-scm.com/download/win")
        return False


def clone_comfyui():
    """Clone ComfyUI repository."""
    comfyui_path = Path("ComfyUI")

    if comfyui_path.exists():
        print(f"ℹ {comfyui_path}/ already exists, skipping clone")
        return True

    print("Cloning ComfyUI...")
    try:
        subprocess.run(
            ["git", "clone", "https://github.com/comfyanonymous/ComfyUI", str(comfyui_path)],
            check=True
        )
        print(f"✓ ComfyUI cloned to {comfyui_path}/")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed to clone ComfyUI: {e}")
        return False


def install_dependencies(port, use_fp32):
    """Install torch-directml and other dependencies into ComfyUI env."""
    comfyui_path = Path("ComfyUI")

    if not comfyui_path.exists():
        print(f"ERROR: {comfyui_path}/ not found. Run without --skip-clone first.")
        return False

    print("Installing torch-directml and dependencies...")

    # Install torch-directml
    deps = [
        "torch-directml",
        "torchvision",
        "Pillow",
        "scipy",
        "einops",
        "transformers",
        "safetensors",
        "omegaconf",
        "tqdm"
    ]

    for dep in deps:
        print(f"  Installing {dep}...")
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", dep],
                check=True,
                capture_output=True
            )
        except subprocess.CalledProcessError as e:
            print(f"  WARNING: Failed to install {dep}: {e}")
            continue

    print("✓ Dependencies installed")
    return True


def create_launch_script(port, use_fp32):
    """Create launch_amd.bat for easy launching."""
    comfyui_path = Path("ComfyUI")
    launch_bat = comfyui_path / "launch_amd.bat"

    fp32_flag = "--fp32" if use_fp32 else ""

    script_content = f"""@echo off
REM ComfyUI AMD Windows Launcher
REM DirectML backend with fp32 for AMD stability

cd /d "%~dp0"
python main.py --directml {fp32_flag} --listen 0.0.0.0 --port {port}
pause
"""

    try:
        launch_bat.write_text(script_content)
        print(f"✓ Created {launch_bat}")
        return True
    except Exception as e:
        print(f"ERROR: Failed to create launch script: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Automate ComfyUI setup for AMD Windows with DirectML"
    )
    parser.add_argument(
        "--skip-clone",
        action="store_true",
        help="Skip cloning ComfyUI (already installed)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8188,
        help="Port for ComfyUI web interface (default: 8188)"
    )
    parser.add_argument(
        "--fp32",
        action="store_true",
        default=True,
        help="Use fp32 precision (default: True for AMD stability)"
    )
    parser.add_argument(
        "--no-fp32",
        action="store_false",
        dest="fp32",
        help="Disable fp32 (use fp16 if supported)"
    )

    args = parser.parse_args()

    print("=" * 60)
    print("ComfyUI AMD Windows Setup")
    print("=" * 60)

    # Check prerequisites
    check_python()
    if not check_git():
        sys.exit(1)

    # Clone ComfyUI if needed
    if not args.skip_clone:
        if not clone_comfyui():
            sys.exit(1)

    # Install dependencies
    if not install_dependencies(args.port, args.fp32):
        sys.exit(1)

    # Create launch script
    if not create_launch_script(args.port, args.fp32):
        sys.exit(1)

    print("=" * 60)
    print("✓ Installation complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. python scripts/verify_gpu.py    # Verify GPU setup")
    print("  2. python scripts/launch.py         # Launch ComfyUI")
    print("  3. Open http://localhost:8188 in your browser")
    print()
    print("Custom nodes:")
    print("  python scripts/install_nodes.py --all")
    print()
    print("Models go in: ComfyUI/models/")
    print()


if __name__ == "__main__":
    main()
