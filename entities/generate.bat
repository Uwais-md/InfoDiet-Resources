@echo off
setlocal enabledelayedexpansion

:: Navigate to the directory containing the batch script
cd /d "%~dp0"

set NUMBER_OF_ENTITIES=5000

:: Find and execute all Python scripts in the repository
for /r %%F in (*.py) do (
    echo Executing %%F
    python "%%F"
)

endlocal