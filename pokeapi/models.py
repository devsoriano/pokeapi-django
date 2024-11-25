from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    types = models.CharField(max_length=200)  # Almacenar tipos separados por comas
    weight = models.IntegerField()
    abilities = models.CharField(max_length=300)  # Almacenar habilidades separadas por comas
    image_front = models.URLField()  # Imagen frontal
    image_back = models.URLField()   # Imagen trasera

    def __str__(self):
        return self.name
