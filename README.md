# 📥 Evor-Descarga tu Video con Docker

Aplicación web desarrollada en Python con Flask que permite descargar videos desde diferentes plataformas como:

- YouTube (limitado por restricciones)
- TikTok
- Instagram
- Facebook
- LinkedIn

---

## 🚀 Tecnologías utilizadas

- Python 3.11
- Flask
- yt-dlp
- Docker

---

## 📦 Estructura del proyecto

.
├── app.py  
├── requirements.txt  
├── Dockerfile  
├── Dockerfile.optimizado  
├── Dockerfile.multistage  
├── .dockerignore  
└── README.md  

---

## ⚙️ ¿Cómo funciona?

El usuario ingresa la URL de un video en la interfaz web.  
La aplicación utiliza la librería `yt-dlp` para descargar el contenido y luego lo envía como archivo descargable.

---

## 🐳 Ejecución con Docker (Paso a paso)

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO

---

🐳 Ejecución básica
Construir imagen
docker build -t video-app:v1 .
Ejecutar contenedor
docker run -p 5000:5000 video-app:v1
Verificar
docker ps
Logs (opcional)
docker logs CONTAINER_ID
Abrir en navegador

http://localhost:5000

---

⚙️ Otras versiones
Dockerfile Optimizado
docker build -f Dockerfile.optimizado -t video-app:v2 .
docker run -p 5000:5000 video-app:v2
Dockerfile Multi-Stage
docker build -f Dockerfile.multistage -t video-app:v3 .
docker run -p 5000:5000 video-app:v3

---

🧪 Comandos útiles
docker images
docker ps
docker stop CONTAINER_ID
docker rm CONTAINER_ID
docker rm -f $(docker ps -aq)

---

⚠️ Limitaciones

YouTube puede bloquear la descarga en entornos cloud debido a medidas anti-bot.
Sin embargo, la aplicación funciona correctamente con otras plataformas como TikTok, Instagram y Facebook.
