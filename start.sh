#!/bin/bash
ls -R /app
set -e  # Detener el script si ocurre un error

# Configurar el PYTHONPATH para que Django encuentre el módulo del proyecto
export PYTHONPATH=/app

echo "Esperando a que PostgreSQL esté listo..."
until pg_isready -h db -p "$POSTGRES_PORT" -U "$POSTGRES_USER" > /dev/null 2>&1; do
  echo "PostgreSQL no está listo, esperando..."
  sleep 2
done
echo "PostgreSQL está listo, continuando..."

echo "Aplicando migraciones pendientes..."
python manage.py migrate --noinput

echo "Verificando si el superusuario existe..."
python manage.py shell <<EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
    print("Superusuario creado: admin / adminpassword")
else:
    print("El superusuario ya existe.")
EOF

echo "Iniciando Celery Worker y Beat..."
celery -A celery_app worker --loglevel=info &
celery -A celery_app beat --loglevel=info &

echo "Ejecutando el job para poblar datos iniciales..."
python manage.py shell <<EOF
from apps.pokemons.tasks import fetch_all_pokemons
fetch_all_pokemons.delay()
EOF

echo "Iniciando el servidor de Django..."
python manage.py runserver 0.0.0.0:8000
