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

# Ejecutar el job de fetch_pokemon_data
echo "Ejecutando el job fetch_pokemon_data..."
python manage.py shell <<EOF
from pokeapi.jobs import fetch_pokemon_data
fetch_pokemon_data()
print("Datos de Pokémon cargados correctamente.")
EOF

# Crear superusuario si no existe
echo "Creando superusuario..."
python manage.py shell <<EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'rafael.soriano@arteenarte.com', 'Un1Tip5?¿xl')
    print("Superusuario 'admin' creado con éxito.")
else:
    print("El superusuario 'admin' ya existe.")
EOF

# Iniciar el servidor
echo "Iniciando el servidor de Django..."
exec python manage.py runserver 0.0.0.0:8000
