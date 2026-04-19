# Contributing to ComfyUI AMD Windows Setup

Thank you for your interest in contributing! This document outlines how to contribute.

## Code of Conduct

- Be respectful and constructive
- Provide helpful feedback
- Respect differing opinions
- Focus on the issue, not the person

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/comfyui-amd-windows-setup.git
   cd comfyui-amd-windows-setup
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b fix/your-issue-name
   # or
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** and commit:
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   ```
5. **Push to your fork**:
   ```bash
   git push origin fix/your-issue-name
   ```
6. **Create a Pull Request** on GitHub

## Guidelines

### Python Scripts

- Use Python 3.10+
- Include docstrings at the top of each script
- Use `argparse` for CLI arguments
- Add usage examples in docstring
- Test cross-platform (Windows, Linux, macOS concepts)

**Example**:
```python
#!/usr/bin/env python3
"""
My Script

Short description of what it does.

Usage:
    python scripts/my_script.py --flag value
    python scripts/my_script.py --all
"""

import argparse
```

### Documentation

- Use Markdown for `.md` files
- Keep language clear and concise
- Include code examples where relevant
- Link to related resources
- Update `CHANGELOG.md` for significant changes

### Commit Messages

Use clear, descriptive messages:
- ✓ "Fix fp16 black image issue on AMD GPUs"
- ✓ "Add DirectML device detection script"
- ✗ "fix bug" or "update stuff"

Format:
```
<verb> <subject>

<optional detailed explanation>
```

### Testing

- Test scripts locally before submitting
- Verify Python syntax: `python -m py_compile scripts/your_script.py`
- Test on Windows (primary platform)
- Mention OS and Python version in PR

## What to Contribute

### Bug Fixes
- Report detailed reproduction steps
- Include GPU model, driver version, Python version
- Attach error messages / screenshots
- Link to related issues

### Features
- Propose feature in an issue first
- Discuss use case and implementation
- Keep scope focused and modular
- Add tests if applicable

### Documentation
- Clarify unclear sections
- Add examples
- Fix typos
- Expand troubleshooting guides

### Node Pack Support
- Add support for new custom nodes
- Update node registry in `scripts/install_nodes.py`
- Test installation and functionality
- Document in `README.md`

## Pull Request Process

1. **Update your branch** with latest main:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Verify tests pass**:
   ```bash
   python -m py_compile scripts/*.py
   ```

3. **Update CHANGELOG.md** under "Unreleased":
   ```markdown
   ## [Unreleased]
   ### Added
   - New feature description

   ### Fixed
   - Bug fix description
   ```

4. **Create descriptive PR**:
   - Explain what it does
   - Reference related issues: "Fixes #123"
   - List testing steps

## Licensing

By contributing, you agree your code is licensed under the MIT License (see LICENSE).

## Recognition

Contributors will be acknowledged in `CHANGELOG.md` and pinned in the repository.

---

Thank you for helping improve ComfyUI AMD Windows Setup!

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/chharith)
