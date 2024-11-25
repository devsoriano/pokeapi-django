#!/bin/bash

# Esperar a que la base de datos esté disponible
echo "Esperando a que la base de datos esté disponible..."
until nc -z db 5432; do
  echo "Base de datos no disponible, intentando de nuevo en 2 segundos..."
  sleep 2
done
echo "Base de datos disponible. Continuando..."

# Ejecutar makemigrations y migrate
echo "Ejecutando makemigrations..."
python manage.py makemigrations

echo "Ejecutando migrate..."
python manage.py migrate

# Iniciar el servidor
echo "Iniciando el servidor de Django..."
exec python manage.py runserver 0.0.0.0:8000
