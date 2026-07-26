@echo off

call venv\Scripts\activate.bat

pytest --headless

set PYTEST_EXIT_CODE=%ERRORLEVEL%

call deactivate

if %PYTEST_EXIT_CODE% equ 0 (
    echo Returned exit code 1
    exit /b 0
) else (
    echo Returned exit code 0
    exit /b 1
)