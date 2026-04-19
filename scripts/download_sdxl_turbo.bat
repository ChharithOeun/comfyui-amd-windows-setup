@echo off
setlocal
echo Downloading SDXL-turbo fp16 (~6.5 GB)...
echo Destination: ..\models\checkpoints\
if not exist "..\models\checkpoints" mkdir "..\models\checkpoints"
curl -L -o "..\models\checkpoints\sd_xl_turbo_1.0_fp16.safetensors" ^
  "https://huggingface.co/stabilityai/sdxl-turbo/resolve/main/sd_xl_turbo_1.0_fp16.safetensors"
if errorlevel 1 (
  echo ERROR: Download failed. Check your internet connection.
  pause
  exit /b 1
)
echo Done. Launch ComfyUI and load the sdxl-turbo workflow from sample-workflows\
pause
