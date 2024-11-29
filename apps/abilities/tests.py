from django.test import TestCase
from apps.abilities.models import Ability

class AbilityModelTests(TestCase):
    def test_create_ability(self):
        # Crear una habilidad
        ability = Ability.objects.create(
            name="Overgrow",
            description="Boosts the power of Grass-type moves in a pinch.",
            short_effect="Increases Grass moves' power."
        )

        # Verificar los valores asignados
        self.assertEqual(ability.name, "Overgrow")
        self.assertEqual(ability.description, "Boosts the power of Grass-type moves in a pinch.")
        self.assertEqual(ability.short_effect, "Increases Grass moves' power.")
        self.assertEqual(str(ability), "Overgrow")
