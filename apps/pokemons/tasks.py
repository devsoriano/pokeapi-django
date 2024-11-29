import requests
from celery import shared_task
from .models import Pokemon
from apps.abilities.models import Ability

@shared_task
def fetch_all_pokemons(start_page=1, end_page=2):
    """
    Job que extrae información de Pokémon de un rango específico de páginas
    desde la PokeAPI, y actualiza o inserta los datos según corresponda.
    """
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    ability_base_url = "https://pokeapi.co/api/v2/ability/"
    results_per_page = 20  # Por defecto, la PokeAPI devuelve 20 resultados por página.

    for page in range(start_page, end_page + 1):
        try:
            # Calcular el rango de IDs en función de la página
            offset = (page - 1) * results_per_page
            response = requests.get(f"{base_url}?offset={offset}&limit={results_per_page}")
            response.raise_for_status()

            data = response.json()

            for pokemon_data in data["results"]:
                pokemon_url = pokemon_data["url"]
                pokemon_response = requests.get(pokemon_url)
                pokemon_response.raise_for_status()
                pokemon_detail = pokemon_response.json()

                # Procesar habilidades y poblar la tabla Ability
                abilities = []
                for ability_info in pokemon_detail["abilities"]:
                    ability_name = ability_info["ability"]["name"]

                    # Obtener o crear la habilidad
                    ability, _ = Ability.objects.get_or_create(
                        name=ability_name,
                        defaults={
                            "description": get_ability_description(ability_base_url, ability_name),
                            "short_effect": get_ability_short_effect(ability_base_url, ability_name),
                        },
                    )
                    abilities.append(ability)

                # Crear o actualizar Pokémon
                pokemon, created = Pokemon.objects.update_or_create(
                    name=pokemon_detail["name"],
                    defaults={
                        "types": ",".join([t["type"]["name"] for t in pokemon_detail["types"]]),
                        "weight": pokemon_detail["weight"],
                        "image_front": pokemon_detail["sprites"].get("front_default", ""),
                        "image_back": pokemon_detail["sprites"].get("back_default", ""),
                    },
                )

                # Relacionar habilidades con el Pokémon
                pokemon.abilities.set(abilities)

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener la página {page}: {e}")
        except Exception as e:
            print(f"Error procesando datos en la página {page}: {e}")



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
