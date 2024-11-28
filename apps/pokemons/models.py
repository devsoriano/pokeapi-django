from django.db import models
from apps.abilities.models import Ability

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    types = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)  # Proporciona un valor predeterminado
    abilities = models.ManyToManyField('abilities.Ability', related_name="pokemons")
    image_front = models.URLField(blank=True, null=True)
    image_back = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

