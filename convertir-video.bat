@echo off
echo ========================================
echo Convertidor de Video para Asistente GEA
echo ========================================
echo.

REM Verificar si FFmpeg está instalado
where ffmpeg >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] FFmpeg no está instalado o no está en el PATH
    echo.
    echo Para instalar FFmpeg:
    echo 1. Descarga FFmpeg desde: https://ffmpeg.org/download.html
    echo 2. O usa chocolatey: choco install ffmpeg
    echo 3. O descarga el build de: https://www.gyan.dev/ffmpeg/builds/
    echo.
    echo Después de instalar, reinicia este script.
    pause
    exit /b 1
)

echo [OK] FFmpeg encontrado
echo.

REM Verificar que el video original existe
if not exist "animacion_carga.mp4" (
    echo [ERROR] No se encontró el archivo: animacion_carga.mp4
    echo Asegúrate de que el video esté en la carpeta raíz del proyecto.
    pause
    exit /b 1
)

echo [INFO] Video original encontrado
echo [INFO] Convirtiendo video a formato compatible (H.264/AAC)...
echo.

REM Crear carpeta temporal si no existe
if not exist "temp" mkdir temp

REM Convertir el video
ffmpeg -i "animacion_carga.mp4" ^
    -c:v libx264 ^
    -preset medium ^
    -crf 23 ^
    -c:a aac ^
    -b:a 128k ^
    -movflags +faststart ^
    -pix_fmt yuv420p ^
    "temp\animacion_carga_converted.mp4"

if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Error al convertir el video
    pause
    exit /b 1
)

echo.
echo [OK] Video convertido exitosamente
echo.

REM Copiar el video convertido a la carpeta public
if not exist "frontend\public\videos" mkdir "frontend\public\videos"
copy /Y "temp\animacion_carga_converted.mp4" "frontend\public\videos\animacion_carga.mp4"

if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Error al copiar el video a la carpeta public
    pause
    exit /b 1
)

echo [OK] Video copiado a frontend\public\videos\animacion_carga.mp4
echo.
echo [COMPLETADO] El video está listo para usar
echo.
echo Puedes eliminar la carpeta "temp" si lo deseas.
echo.
pause

