# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema, incluyendo netcat-openbsd, gcc y libpq-dev
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    gcc \
    libpq-dev && apt-get clean

# Copia y configura dependencias de Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del proyecto al contenedor
COPY . .

# Expone el puerto 8000 para Django
EXPOSE 8000

# Añade un script de shell para ejecutar las migraciones y luego iniciar el servidor
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Usa el script como comando de inicio
CMD ["/entrypoint.sh"]
