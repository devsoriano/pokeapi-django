from rest_framework import serializers
from .models import Pokemon
from apps.abilities.serializers import AbilitySerializer

class PokemonSerializer(serializers.ModelSerializer):
    abilities = AbilitySerializer(many=True, read_only=True)  # Habilidades son de solo lectura

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'types', 'weight', 'abilities', 'image_front', 'image_back']
