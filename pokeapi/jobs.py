import requests
from .models import Pokemon


def fetch_pokemon_data():
    # Eliminar todos los datos existentes en la tabla
    Pokemon.objects.all().delete()

    base_url = "https://pokeapi.co/api/v2/pokemon/"
    for page in range(1, 3):  # Dos páginas (40 Pokémon)
        response = requests.get(f"{base_url}?offset={(page - 1) * 20}&limit=20")
        if response.status_code == 200:
            data = response.json()
            for item in data['results']:
                # Obtener detalles individuales del Pokémon
                pokemon_detail = requests.get(item['url']).json()

                # Extraer tipos
                types = [t['type']['name'] for t in pokemon_detail['types']]

                # Extraer habilidades
                abilities = [a['ability']['name'] for a in pokemon_detail['abilities']]

                # Extraer imágenes (sin incluir las de 'other')
                sprites = pokemon_detail['sprites']
                image_front = sprites.get('front_default', '')
                image_back = sprites.get('back_default', '')

                # Guardar en la base de datos
                Pokemon.objects.create(
                    name=pokemon_detail['name'],
                    types=",".join(types),
                    weight=pokemon_detail['weight'],
                    abilities=",".join(abilities),
                    image_front=image_front,
                    image_back=image_back,
                )
        else:
            print(f"Error fetching data from {base_url}: {response.status_code}")
