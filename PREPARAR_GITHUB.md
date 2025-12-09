# 📤 Preparar y Subir Proyecto a GitHub

Sigue estos pasos para subir tu proyecto a GitHub:

## Paso 1: Verificar que no haya archivos sensibles

```bash
# Verifica que no haya archivos .env
git status
```

Si ves archivos `.env`, asegúrate de que estén en `.gitignore`.

## Paso 2: Inicializar Git (si no está inicializado)

```bash
git init
```

## Paso 3: Agregar todos los archivos

```bash
git add .
```

## Paso 4: Hacer el primer commit

```bash
git commit -m "Initial commit: Asistente GEA - Proyecto completo con backend y frontend"
```

## Paso 5: Crear repositorio en GitHub

1. Ve a https://github.com
2. Click en **"New"** (o el botón **"+"** en la esquina superior derecha)
3. **Nombre del repositorio**: `asistente-gea` (o el nombre que prefieras)
4. **Descripción**: "Asistente Inteligente para el Sistema GEA - Proyecto Final"
5. **Visibilidad**: Público o Privado (tu elección)
6. **NO marques**: "Add a README file", "Add .gitignore", "Choose a license" (ya los tenemos)
7. Click en **"Create repository"**

## Paso 6: Conectar y subir a GitHub

GitHub te mostrará comandos. Ejecuta estos:

```bash
git remote add origin https://github.com/TU-USUARIO/asistente-gea.git
git branch -M main
git push -u origin main
```

**Reemplaza `TU-USUARIO` con tu nombre de usuario de GitHub.**

## Paso 7: Verificar

Ve a tu repositorio en GitHub y verifica que todos los archivos estén ahí.

## ✅ Listo

Una vez subido, puedes continuar con el despliegue en Render y Vercel siguiendo `GUIA_DESPLIEGUE.md`.

