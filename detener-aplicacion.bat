@echo off
echo ========================================
echo   Deteniendo Asistente GEA
echo ========================================
echo.

echo Deteniendo procesos de Python (Backend)...
taskkill /FI "WINDOWTITLE eq Asistente GEA - Backend*" /T /F >nul 2>&1
taskkill /FI "IMAGENAME eq python.exe" /FI "WINDOWTITLE eq *uvicorn*" /T /F >nul 2>&1
taskkill /FI "IMAGENAME eq uvicorn.exe" /T /F >nul 2>&1

echo Deteniendo procesos de Node.js (Frontend)...
taskkill /FI "WINDOWTITLE eq Asistente GEA - Frontend*" /T /F >nul 2>&1
taskkill /FI "IMAGENAME eq node.exe" /FI "WINDOWTITLE eq *vite*" /T /F >nul 2>&1

REM Detener procesos en los puertos específicos
echo Liberando puertos 8000 y 3000...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000 ^| findstr LISTENING') do (
    taskkill /F /PID %%a >nul 2>&1
)
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3000 ^| findstr LISTENING') do (
    taskkill /F /PID %%a >nul 2>&1
)

echo.
echo Procesos detenidos correctamente
echo.
pause

