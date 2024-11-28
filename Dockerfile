# Imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Evitar interacción en la instalación de paquetes
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de requerimientos e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Dar permisos de ejecución al archivo start.sh
RUN chmod +x ./start.sh

# Exponer el puerto de Django
EXPOSE 8000

# Comando principal
CMD ["sh", "./start.sh"]
