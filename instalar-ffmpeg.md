# Instalación de FFmpeg para Windows

FFmpeg es necesario para convertir el video de animación a un formato compatible con los navegadores web.

## Opción 1: Instalación con Chocolatey (Recomendado)

Si tienes Chocolatey instalado:

```powershell
choco install ffmpeg
```

## Opción 2: Instalación Manual

1. **Descargar FFmpeg:**
   - Ve a: https://www.gyan.dev/ffmpeg/builds/
   - Descarga "ffmpeg-release-essentials.zip"
   - O usa el enlace directo: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip

2. **Extraer y configurar:**
   - Extrae el archivo ZIP
   - Copia la carpeta `ffmpeg-x.x.x-essentials_build` a `C:\ffmpeg`
   - Agrega `C:\ffmpeg\bin` al PATH del sistema:
     - Abre "Variables de entorno" en Windows
     - Edita la variable "Path"
     - Agrega: `C:\ffmpeg\bin`
     - Acepta y reinicia la terminal

3. **Verificar instalación:**
   ```powershell
   ffmpeg -version
   ```

## Opción 3: Usar FFmpeg Portable (Sin instalación)

1. Descarga FFmpeg portable desde: https://www.gyan.dev/ffmpeg/builds/
2. Extrae en una carpeta (ej: `C:\ffmpeg-portable`)
3. Usa la ruta completa en el script:
   ```batch
   C:\ffmpeg-portable\bin\ffmpeg.exe -i "animacion_carga.mp4" ...
   ```

## Opción 4: Conversión Online (Alternativa)

Si no puedes instalar FFmpeg, puedes usar conversores online:

1. **CloudConvert:** https://cloudconvert.com/mp4-converter
2. **FreeConvert:** https://www.freeconvert.com/mp4-converter
3. **Zamzar:** https://www.zamzar.com/convert/mp4-to-mp4/

**Configuración recomendada:**
- Formato: MP4
- Codec de video: H.264
- Codec de audio: AAC
- Calidad: Media/Alta

## Después de instalar FFmpeg

1. Ejecuta `convertir-video.bat` desde la carpeta raíz del proyecto
2. El script convertirá automáticamente el video y lo copiará a la ubicación correcta

