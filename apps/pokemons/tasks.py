import requests
from celery import shared_task
from .models import Pokemon
from apps.abilities.models import Ability


@shared_task
def fetch_all_pokemons():
    """
    Job que extrae información de los primeros 150 Pokémon desde la PokeAPI
    y los almacena en la base de datos.
    """
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    ability_base_url = "https://pokeapi.co/api/v2/ability/"

    for pokemon_id in range(1, 151):
        try:
            response = requests.get(f"{base_url}{pokemon_id}/")
            response.raise_for_status()

            data = response.json()

            # Procesar habilidades y poblar la tabla Ability
            abilities = []
            for ability_info in data["abilities"]:
                ability_name = ability_info["ability"]["name"]

                # Si la habilidad no existe, obtener la descripción de la API de habilidades
                if not Ability.objects.filter(name=ability_name).exists():
                    ability_response = requests.get(f"{ability_base_url}{ability_name}/")
                    ability_response.raise_for_status()
                    ability_data = ability_response.json()

                    Ability.objects.create(
                        name=ability_name,
                        description=next(
                            (entry["effect"] for entry in ability_data["effect_entries"] if
                             entry["language"]["name"] == "en"),
                            "No description available"
                        ),
                        short_effect=next(
                            (entry["short_effect"] for entry in ability_data["effect_entries"] if
                             entry["language"]["name"] == "en"),
                            "No short description available"
                        )
                    )
                abilities.append(ability_name)

            # Crear o actualizar Pokémon con habilidades relacionadas
            Pokemon.objects.update_or_create(
                id=pokemon_id,
                defaults={
                    "name": data["name"],
                    "types": [t["type"]["name"] for t in data["types"]],
                    "abilities": ",".join(abilities),
                    "sprites": data["sprites"]["front_default"],
                }
            )
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener el Pokémon con ID {pokemon_id}: {e}")
        except Exception as e:
            print(f"Error procesando el Pokémon con ID {pokemon_id}: {e}")
