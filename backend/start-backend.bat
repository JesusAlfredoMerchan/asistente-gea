@echo off
cd /d "%~dp0"
echo ========================================
echo   Asistente GEA - Backend
echo ========================================
echo.
echo Iniciando servidor en http://localhost:8000
echo.
if exist "venv\Scripts\python.exe" (
    venv\Scripts\python.exe -m uvicorn main:app --reload --port 8000
) else (
    echo ERROR: No se encuentra el entorno virtual
    echo Por favor, ejecuta iniciar-aplicacion.bat desde la raiz del proyecto
    pause
)

