---
name: Bug Report
about: Report a bug or unexpected behavior
title: "[BUG] "
labels: bug
assignees: ''

---

## Description
<!-- Clear and concise description of the bug -->

## Steps to Reproduce
1. <!-- First step -->
2. <!-- Second step -->
3. <!-- etc. -->

## Expected Behavior
<!-- What you expected to happen -->

## Actual Behavior
<!-- What actually happened -->

## System Information
- **OS**: Windows
- **Windows Version**: <!-- e.g., Windows 10, Windows 11 -->
- **Python Version**: <!-- e.g., 3.10, 3.11, 3.12 -->
- **GPU Model**: <!-- e.g., Radeon RX 6700 XT -->
- **AMD Driver Version**: <!-- e.g., 24.5.1 (run `dxdiag` to check) -->
- **torch-directml Version**: <!-- e.g., 1.13.0 -->

## ComfyUI Setup
- **ComfyUI Version**: <!-- Check in ComfyUI repo, or "Latest" -->
- **Custom Nodes Installed**: <!-- List nodes, e.g., ComfyUI-Manager, Impact-Pack, etc. -->
  - <!-- Node 1 -->
  - <!-- Node 2 -->
  - <!-- etc. -->

## Error Output
<!-- Paste any error messages, stack traces, or console output -->
```
[Paste error here]
```

## Screenshots
<!-- If applicable, attach screenshots of the issue or ComfyUI UI -->

## GPU Verification
<!-- Run: python scripts/verify_gpu.py and paste output -->
```
[Paste output here]
```

## Additional Context
<!-- Any other relevant information -->

---

**Quick Checklist**:
- [ ] AMD drivers are up to date (`dxdiag` → Display tab)
- [ ] Python 3.10+ is installed
- [ ] torch-directml is installed (`pip install torch-directml`)
- [ ] ComfyUI was installed via `python scripts/install.py`
- [ ] `python scripts/verify_gpu.py` runs without errors
