@echo off

echo ------------------
echo Load local/default Settings
echo ------------------

set DEFAULT_CONFIG_FILE=%~dp0\config\default_config.bat
set LOCAL_CONFIG_FILE=%~dp0\config\local_config.bat

if exist %LOCAL_CONFIG_FILE% (
    call %LOCAL_CONFIG_FILE%
) else (
    call %DEFAULT_CONFIG_FILE%
)

rem Run sub Script
set PS_INSTALL_PATH=%~dp0private\install_SeamCMD.ps1
PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& '%PS_INSTALL_PATH%'"

pause