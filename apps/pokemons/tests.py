from django.test import TestCase
from .models import Pokemon
from apps.abilities.models import Ability

class PokemonModelTests(TestCase):
    def test_create_pokemon_with_abilities(self):
        ability = Ability.objects.create(name="Overgrow", is_hidden=False)
        pokemon = Pokemon.objects.create(
            name="Bulbasaur",
            sprites={"front_default": "url-to-image"},
            types=["grass", "poison"]
        )
        pokemon.abilities.add(ability)
        self.assertEqual(str(pokemon), "Bulbasaur")
