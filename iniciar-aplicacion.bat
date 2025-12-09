@echo off
cd /d "%~dp0"

echo ========================================
echo   Iniciando Asistente GEA
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado
    pause
    exit /b 1
)

node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js no está instalado
    pause
    exit /b 1
)

echo [1/4] Verificando backend...
if not exist "backend\requirements.txt" (
    echo [ERROR] No se encuentra requirements.txt
    pause
    exit /b 1
)

if not exist "backend\venv" (
    echo [INFO] Creando entorno virtual...
    python -m venv backend\venv
    if errorlevel 1 (
        echo [ERROR] Error al crear entorno virtual
        pause
        exit /b 1
    )
)

echo [2/4] Instalando dependencias backend...
backend\venv\Scripts\python.exe -m pip install -q -r backend\requirements.txt
if errorlevel 1 (
    echo [ERROR] Error instalando dependencias backend
    pause
    exit /b 1
)

echo [3/4] Verificando frontend...
if not exist "frontend\package.json" (
    echo [ERROR] No se encuentra package.json
    pause
    exit /b 1
)

if not exist "frontend\node_modules" (
    echo [INFO] Instalando dependencias frontend...
    cd frontend
    call npm install
    if errorlevel 1 (
        echo [ERROR] Error instalando dependencias frontend
        pause
        exit /b 1
    )
    cd ..
)

echo [4/4] Iniciando servidores...
echo.
echo ========================================
echo   Backend: http://localhost:8000
echo   Frontend: http://localhost:3000
echo ========================================
echo.

start "Asistente GEA - Backend" cmd /k "cd /d %~dp0backend && start-backend.bat"
ping 127.0.0.1 -n 4 >nul
start "Asistente GEA - Frontend" cmd /k "cd /d %~dp0frontend && start-frontend.bat"

echo Servidores iniciados!
echo.
echo Esperando a que el frontend esté listo...
REM Esperar un poco más para que el servidor frontend esté completamente iniciado
ping 127.0.0.1 -n 6 >nul

echo Abriendo navegador en http://localhost:3000...
start "" http://localhost:3000

echo.
echo La aplicación se ha abierto en tu navegador
echo.
pause
