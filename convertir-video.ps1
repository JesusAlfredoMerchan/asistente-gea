# Script PowerShell para convertir video con FFmpeg
# Convertidor de Video para Asistente GEA

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Convertidor de Video para Asistente GEA" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si FFmpeg está instalado
$ffmpegPath = Get-Command ffmpeg -ErrorAction SilentlyContinue

if (-not $ffmpegPath) {
    Write-Host "[ERROR] FFmpeg no está instalado o no está en el PATH" -ForegroundColor Red
    Write-Host ""
    Write-Host "Para instalar FFmpeg:" -ForegroundColor Yellow
    Write-Host "1. Descarga FFmpeg desde: https://ffmpeg.org/download.html" -ForegroundColor White
    Write-Host "2. O usa chocolatey: choco install ffmpeg" -ForegroundColor White
    Write-Host "3. O descarga el build de: https://www.gyan.dev/ffmpeg/builds/" -ForegroundColor White
    Write-Host ""
    Write-Host "Ver archivo 'instalar-ffmpeg.md' para más detalles." -ForegroundColor Yellow
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host "[OK] FFmpeg encontrado: $($ffmpegPath.Source)" -ForegroundColor Green
Write-Host ""

# Verificar que el video original existe
$videoOriginal = "animacion_carga.mp4"
if (-not (Test-Path $videoOriginal)) {
    Write-Host "[ERROR] No se encontró el archivo: $videoOriginal" -ForegroundColor Red
    Write-Host "Asegúrate de que el video esté en la carpeta raíz del proyecto." -ForegroundColor Yellow
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host "[INFO] Video original encontrado: $videoOriginal" -ForegroundColor Cyan
$fileSize = (Get-Item $videoOriginal).Length / 1MB
Write-Host "[INFO] Tamaño: $([math]::Round($fileSize, 2)) MB" -ForegroundColor Cyan
Write-Host "[INFO] Convirtiendo video a formato compatible (H.264/AAC)..." -ForegroundColor Cyan
Write-Host ""

# Crear carpeta temporal si no existe
$tempDir = "temp"
if (-not (Test-Path $tempDir)) {
    New-Item -ItemType Directory -Path $tempDir | Out-Null
}

$videoConvertido = "$tempDir\animacion_carga_converted.mp4"

# Convertir el video
Write-Host "Ejecutando FFmpeg..." -ForegroundColor Yellow
$ffmpegArgs = @(
    "-i", "`"$videoOriginal`"",
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "23",
    "-c:a", "aac",
    "-b:a", "128k",
    "-movflags", "+faststart",
    "-pix_fmt", "yuv420p",
    "-y",  # Sobrescribir archivo si existe
    "`"$videoConvertido`""
)

$process = Start-Process -FilePath "ffmpeg" -ArgumentList $ffmpegArgs -NoNewWindow -Wait -PassThru

if ($process.ExitCode -ne 0) {
    Write-Host "[ERROR] Error al convertir el video (Código: $($process.ExitCode))" -ForegroundColor Red
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host ""
Write-Host "[OK] Video convertido exitosamente" -ForegroundColor Green
$newFileSize = (Get-Item $videoConvertido).Length / 1MB
Write-Host "[INFO] Tamaño del video convertido: $([math]::Round($newFileSize, 2)) MB" -ForegroundColor Cyan
Write-Host ""

# Crear carpeta de destino si no existe
$destDir = "frontend\public\videos"
if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
}

# Copiar el video convertido a la carpeta public
$destFile = "$destDir\animacion_carga.mp4"
Copy-Item -Path $videoConvertido -Destination $destFile -Force

if (-not (Test-Path $destFile)) {
    Write-Host "[ERROR] Error al copiar el video a la carpeta public" -ForegroundColor Red
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host "[OK] Video copiado a: $destFile" -ForegroundColor Green
Write-Host ""
Write-Host "[COMPLETADO] El video está listo para usar" -ForegroundColor Green
Write-Host ""
Write-Host "Puedes eliminar la carpeta 'temp' si lo deseas." -ForegroundColor Yellow
Write-Host ""
Read-Host "Presiona Enter para salir"

