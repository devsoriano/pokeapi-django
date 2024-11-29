from django.test import TestCase
from apps.pokemons.models import Pokemon
from apps.abilities.models import Ability

class PokemonModelTests(TestCase):
    def test_create_pokemon_with_abilities(self):
        # Crear una habilidad
        ability = Ability.objects.create(
            name="Overgrow",
            description="Boosts the power of Grass-type moves in a pinch.",
            short_effect="Increases Grass moves' power."
        )

        # Crear un Pokémon
        pokemon = Pokemon.objects.create(
            name="Bulbasaur",
            types="Grass, Poison",
            weight=69,
            image_front="https://example.com/front.png",
            image_back="https://example.com/back.png"
        )

        # Asignar habilidades al Pokémon
        pokemon.abilities.add(ability)

        # Verificar que el Pokémon y la habilidad se crearon correctamente
        self.assertEqual(pokemon.name, "Bulbasaur")
        self.assertEqual(pokemon.types, "Grass, Poison")
        self.assertEqual(pokemon.weight, 69)
        self.assertEqual(pokemon.image_front, "https://example.com/front.png")
        self.assertEqual(pokemon.image_back, "https://example.com/back.png")
        self.assertIn(ability, pokemon.abilities.all())
        self.assertEqual(str(pokemon), "Bulbasaur")
