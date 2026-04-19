@echo off
setlocal
echo Downloading Stable Diffusion 1.5 pruned (~2 GB)...
echo Destination: ..\models\checkpoints\
if not exist "..\models\checkpoints" mkdir "..\models\checkpoints"
curl -L -o "..\models\checkpoints\v1-5-pruned-emaonly.safetensors" ^
  "https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors"
if errorlevel 1 (
  echo ERROR: Download failed. Check your internet connection.
  pause
  exit /b 1
)
echo Done. Launch ComfyUI and select v1-5-pruned-emaonly as your checkpoint.
pause
