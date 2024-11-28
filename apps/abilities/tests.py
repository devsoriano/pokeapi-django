from django.test import TestCase
from .models import Ability

class AbilityModelTests(TestCase):
    def test_create_ability(self):
        ability = Ability.objects.create(name="Overgrow", is_hidden=False)
        self.assertEqual(str(ability), "Overgrow")
