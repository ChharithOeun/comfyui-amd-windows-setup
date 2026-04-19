@echo off
REM ComfyUI AMD Windows Setup Menu
REM Interactive menu for installation, launching, and setup

setlocal enabledelayedexpansion

:menu
cls
echo.
echo ============================================================
echo       ComfyUI AMD Windows Setup Menu
echo ============================================================
echo.
echo   1. Install ComfyUI (DirectML backend)
echo   2. Launch ComfyUI
echo   3. Verify GPU Setup
echo   4. Install Custom Nodes
echo   5. Exit
echo.
echo ============================================================
echo.

set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo.
    python scripts\install.py
    pause
    goto menu
)

if "%choice%"=="2" (
    echo.
    python scripts\launch.py
    goto menu
)

if "%choice%"=="3" (
    echo.
    python scripts\verify_gpu.py
    pause
    goto menu
)

if "%choice%"=="4" (
    echo.
    python scripts\install_nodes.py --all
    pause
    goto menu
)

if "%choice%"=="5" (
    echo.
    echo Goodbye!
    exit /b 0
)

echo Invalid choice. Please try again.
pause
goto menu
