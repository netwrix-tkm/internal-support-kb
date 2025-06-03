@echo off
REM Script to list available products and then run the KB tool

REM Get script directory
SET SCRIPT_DIR=%~dp0
SET PARENT_DIR=%SCRIPT_DIR%..

REM Ensure we're using the virtual environment if it exists
IF EXIST "%PARENT_DIR%\.venv\Scripts\activate.bat" (
    call "%PARENT_DIR%\.venv\Scripts\activate.bat"
    echo Activated virtual environment
)

REM Check arguments
IF "%~1"=="" (
    echo Usage: %0 ^<stage^>
    echo   stage: 1 or 2
    exit /b 1
)

SET STAGE=%~1

REM List available products
echo Listing available products for stage %STAGE%...
python "%SCRIPT_DIR%list_products.py" --stage %STAGE%

IF %ERRORLEVEL% NEQ 0 (
    echo Failed to list products. Trying alternative approach...
    cd "%PARENT_DIR%"
    python -m internal_kb_tools.list_products --stage %STAGE%
    
    IF %ERRORLEVEL% NEQ 0 (
        echo Error listing products. Please check your setup.
        exit /b 1
    )
)

REM Ask for product path
echo.
set /p PRODUCT_PATH=Enter product path from the list above (e.g. 'Netwrix Endpoint Protector/Device Control/Custom Classes'): 

REM Run the KB tool
echo Running KB tool stage %STAGE% for path: %PRODUCT_PATH%
python "%PARENT_DIR%\run_kb_tool.py" --stage %STAGE% --path "%PRODUCT_PATH%"

IF %ERRORLEVEL% NEQ 0 (
    echo Failed to run KB tool. Trying alternative approach...
    cd "%PARENT_DIR%"
    python run_kb_tool.py --stage %STAGE% --path "%PRODUCT_PATH%"
) 