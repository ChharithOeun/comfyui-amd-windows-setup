#!/usr/bin/env python3
"""
ComfyUI AMD Windows Launcher

Launches ComfyUI with AMD-optimized settings (DirectML, fp32 by default).

Usage:
    python scripts/launch.py                 # Default: port 8188, fp32 enabled
    python scripts/launch.py --port 8080    # Custom port
    python scripts/launch.py --no-fp32       # Disable fp32 (use fp16)
    python scripts/launch.py --cpu           # Force CPU mode
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def check_comfyui_installed():
    """Verify ComfyUI is installed at ./ComfyUI/"""
    comfyui_path = Path("ComfyUI")

    if not comfyui_path.exists():
        print("ERROR: ComfyUI not found at ./ComfyUI/")
        print()
        print("Run first:")
        print("  python scripts/install.py")
        return False

    main_py = comfyui_path / "main.py"
    if not main_py.exists():
        print(f"ERROR: ComfyUI main.py not found at {main_py}")
        return False

    return True


def build_command(port, use_fp32, use_cpu):
    """Build the ComfyUI launch command."""
    comfyui_path = Path("ComfyUI")
    main_py = comfyui_path / "main.py"

    cmd = [
        sys.executable,
        str(main_py),
        "--listen", "0.0.0.0",
        "--port", str(port),
    ]

    if use_cpu:
        print("ℹ CPU mode forced (--cpu)")
        # No device flag = CPU fallback
    else:
        cmd.extend(["--directml"])
        if use_fp32:
            cmd.extend(["--fp32"])
            print("ℹ DirectML with fp32 (AMD optimized)")
        else:
            print("ℹ DirectML with fp16")

    return cmd


def main():
    parser = argparse.ArgumentParser(
        description="Launch ComfyUI with AMD-optimized settings"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8188,
        help="Port for web interface (default: 8188)"
    )
    parser.add_argument(
        "--no-fp32",
        action="store_false",
        dest="fp32",
        default=True,
        help="Disable fp32 (use fp16 if supported)"
    )
    parser.add_argument(
        "--cpu",
        action="store_true",
        help="Force CPU mode (no GPU)"
    )

    args = parser.parse_args()

    if not check_comfyui_installed():
        sys.exit(1)

    print("=" * 60)
    print("ComfyUI AMD Windows Launcher")
    print("=" * 60)
    print()

    cmd = build_command(args.port, args.fp32, args.cpu)

    print(f"Launching ComfyUI on port {args.port}...")
    print(f"Open: http://localhost:{args.port}")
    print()
    print("-" * 60)

    try:
        subprocess.run(cmd, check=False)
    except KeyboardInterrupt:
        print()
        print("ComfyUI stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"ERROR: Failed to launch ComfyUI: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
