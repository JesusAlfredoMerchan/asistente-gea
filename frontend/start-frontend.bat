@echo off
cd /d "%~dp0"
echo ========================================
echo   Asistente GEA - Frontend
echo ========================================
echo.
echo Iniciando servidor en http://localhost:3000
echo.
if exist "package.json" (
    npm run dev
) else (
    echo ERROR: No se encuentra package.json
    echo Por favor, ejecuta iniciar-aplicacion.bat desde la raiz del proyecto
    pause
)

