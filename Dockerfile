# Usar una imagen base de Python
FROM python:3.12-slim

# Instalar dependencias
RUN pip install flask opencv-python-headless Pillow

# Copiar el archivo del servidor Flask al contenedor
COPY server.py /app/server.py

# Establecer variables de entorno necesarias para Flask
# ENV FLASK_APP=/app/server.py
# ENV FLASK_RUN_HOST=0.0.0.0

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar el servidor Flask
CMD ["python", "/app/server.py"]
