from rest_framework import serializers
from .models import Pokemon
from apps.abilities.models import Ability

class PokemonSerializer(serializers.ModelSerializer):
    abilities = serializers.PrimaryKeyRelatedField(
        many=True,  # Permitir múltiples relaciones
        queryset=Ability.objects.all()  # Consultar todas las habilidades disponibles
    )

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'types', 'weight', 'abilities', 'image_front', 'image_back']
