import requests
from celery import shared_task
from .models import Pokemon
from apps.abilities.models import Ability


@shared_task
def fetch_all_pokemons():
    """
    Job que extrae información de los primeros 150 Pokémon desde la PokeAPI,
    eliminando los datos existentes antes de poblar la base de datos.
    """
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    ability_base_url = "https://pokeapi.co/api/v2/ability/"

    # Eliminar todos los datos existentes en las tablas antes de agregar nuevos
    Pokemon.objects.all().delete()
    Ability.objects.all().delete()

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
                ability, created = Ability.objects.get_or_create(
                    name=ability_name,
                    defaults={
                        "description": get_ability_description(ability_base_url, ability_name),
                        "short_effect": get_ability_short_effect(ability_base_url, ability_name),
                    },
                )
                abilities.append(ability)

            # Crear o actualizar Pokémon
            pokemon = Pokemon.objects.create(
                name=data["name"],
                types=",".join([t["type"]["name"] for t in data["types"]]),
                weight=data["weight"],
                image_front=data["sprites"].get("front_default", ""),
                image_back=data["sprites"].get("back_default", ""),
            )

            # Relacionar habilidades con el Pokémon
            pokemon.abilities.set(abilities)

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener el Pokémon con ID {pokemon_id}: {e}")
        except Exception as e:
            print(f"Error procesando el Pokémon con ID {pokemon_id}: {e}")


def get_ability_description(base_url, ability_name):
    """
    Obtener la descripción de una habilidad desde la API de habilidades.
    """
    try:
        ability_response = requests.get(f"{base_url}{ability_name}/")
        ability_response.raise_for_status()
        ability_data = ability_response.json()
        return next(
            (entry["effect"] for entry in ability_data["effect_entries"] if entry["language"]["name"] == "en"),
            "No description available"
        )
    except Exception:
        return "No description available"


def get_ability_short_effect(base_url, ability_name):
    """
    Obtener el short_effect de una habilidad desde la API de habilidades.
    """
    try:
        ability_response = requests.get(f"{base_url}{ability_name}/")
        ability_response.raise_for_status()
        ability_data = ability_response.json()
        return next(
            (entry["short_effect"] for entry in ability_data["effect_entries"] if entry["language"]["name"] == "en"),
            "No short description available"
        )
    except Exception:
        return "No short description available"
