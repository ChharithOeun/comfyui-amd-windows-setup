#!/usr/bin/env python3
"""
Install ComfyUI Custom Nodes

Installs popular custom nodes useful for AMD workflows.

Popular nodes:
  - ComfyUI-Manager: Node pack manager
  - ComfyUI-Impact-Pack: Advanced upscaling, face detection, etc.
  - was-node-suite-comfyui: Image processing and utilities
  - controlnet-aux: ControlNet preprocessors (canny, depth, pose, etc.)

Usage:
    python scripts/install_nodes.py --all                    # Install all popular nodes
    python scripts/install_nodes.py --node ComfyUI-Manager   # Install specific node
    python scripts/install_nodes.py --list                   # List available nodes
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


# Registry of popular nodes with their GitHub URLs
POPULAR_NODES = {
    "ComfyUI-Manager": "https://github.com/ltdrdata/ComfyUI-Manager",
    "ComfyUI-Impact-Pack": "https://github.com/ltdrdata/ComfyUI-Impact-Pack",
    "was-node-suite-comfyui": "https://github.com/WASasquatch/was-node-suite-comfyui",
    "controlnet-aux": "https://github.com/Fannovel16/comfyui_controlnet_aux",
}


def check_comfyui_installed():
    """Verify ComfyUI is installed."""
    comfyui_path = Path("ComfyUI")
    custom_nodes_path = comfyui_path / "custom_nodes"

    if not custom_nodes_path.exists():
        print(f"ERROR: ComfyUI not found at {comfyui_path}/")
        print()
        print("Run first:")
        print("  python scripts/install.py")
        return False, None

    return True, custom_nodes_path


def check_git():
    """Verify git is installed."""
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("ERROR: Git not found. Install from https://git-scm.com/download/win")
        return False


def install_node(node_name, node_url, custom_nodes_path):
    """Clone a custom node into custom_nodes directory."""
    node_path = custom_nodes_path / node_name

    if node_path.exists():
        print(f"ℹ {node_name}/ already exists, skipping")
        return True

    print(f"Installing {node_name}...")

    try:
        subprocess.run(
            ["git", "clone", node_url, str(node_path)],
            check=True,
            capture_output=True
        )
        print(f"  ✓ {node_name} installed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Failed to install {node_name}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Install ComfyUI custom nodes"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Install all popular nodes"
    )
    parser.add_argument(
        "--node",
        type=str,
        help="Install a specific node by name"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available nodes"
    )

    args = parser.parse_args()

    if args.list:
        print("Available nodes:")
        for name in sorted(POPULAR_NODES.keys()):
            print(f"  - {name}")
        return

    print("=" * 60)
    print("ComfyUI Custom Node Installer")
    print("=" * 60)
    print()

    comfyui_ok, custom_nodes_path = check_comfyui_installed()
    if not comfyui_ok:
        sys.exit(1)

    if not check_git():
        sys.exit(1)

    print(f"Installing to: {custom_nodes_path}/")
    print()

    installed = 0
    failed = 0

    if args.all:
        nodes_to_install = POPULAR_NODES.items()
    elif args.node:
        if args.node not in POPULAR_NODES:
            print(f"ERROR: Node '{args.node}' not found")
            print()
            print("Available nodes:")
            for name in sorted(POPULAR_NODES.keys()):
                print(f"  - {name}")
            sys.exit(1)
        nodes_to_install = [(args.node, POPULAR_NODES[args.node])]
    else:
        print("Specify --all to install all nodes, or --node <name> for specific node")
        print()
        print("Available nodes:")
        for name in sorted(POPULAR_NODES.keys()):
            print(f"  - {name}")
        return

    for node_name, node_url in sorted(nodes_to_install):
        if install_node(node_name, node_url, custom_nodes_path):
            installed += 1
        else:
            failed += 1

    print()
    print("=" * 60)
    print(f"Installation summary: {installed} installed, {failed} failed")
    print("=" * 60)
    print()

    if failed == 0:
        print("✓ All nodes installed successfully!")
        print()
        print("Restart ComfyUI to load new nodes.")
    else:
        print("⚠ Some nodes failed. Check errors above.")

    print()


if __name__ == "__main__":
    main()
