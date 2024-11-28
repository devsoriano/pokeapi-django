from rest_framework import serializers
from .models import Pokemon
from apps.abilities.serializers import AbilitySerializer

class PokemonSerializer(serializers.ModelSerializer):
    abilities = AbilitySerializer(many=True)

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'sprites', 'types', 'abilities']
