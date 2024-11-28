from django.db import models
from apps.abilities.models import Ability

class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    sprites = models.JSONField()  # Almacena imágenes (front, back, etc.)
    types = models.JSONField()  # Lista de tipos
    abilities = models.ManyToManyField(Ability, related_name='pokemons')

    def __str__(self):
        return self.name
