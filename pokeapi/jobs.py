import requests
from .models import Pokemon, Ability

def fetch_pokemon_data():
    # Eliminar todos los datos existentes en las tablas antes de agregar nuevos
    Pokemon.objects.all().delete()
    Ability.objects.all().delete()

    base_url = "https://pokeapi.co/api/v2/pokemon/"
    limit = 20  # Pokémon por página
    total_pokemon = 150  # Número total de Pokémon que queremos procesar
    pages = total_pokemon // limit  # Número de páginas

    for page in range(pages):  # Procesar cada página
        offset = page * limit
        response = requests.get(f"{base_url}?offset={offset}&limit={limit}")
        if response.status_code == 200:
            data = response.json()
            for item in data['results']:
                # Obtener detalles individuales del Pokémon
                pokemon_detail = requests.get(item['url']).json()

                # Extraer tipos
                types = [t['type']['name'] for t in pokemon_detail['types']]

                # Extraer habilidades
                abilities = [a['ability']['name'] for a in pokemon_detail['abilities']]

                # Extraer descripciones de habilidades y guardarlas
                for ability_name in abilities:
                    if not Ability.objects.filter(name=ability_name).exists():
                        ability_detail = requests.get(f"https://pokeapi.co/api/v2/ability/{ability_name}/").json()
                        Ability.objects.create(
                            name=ability_name,
                            description=next(
                                (entry['effect'] for entry in ability_detail['effect_entries'] if entry['language']['name'] == 'en'),
                                "No description available"
                            ),
                            short_effect=next(
                                (entry['short_effect'] for entry in ability_detail['effect_entries'] if entry['language']['name'] == 'en'),
                                "No short description available"
                            ),
                        )

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
