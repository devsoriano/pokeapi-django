from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pokemon
from .serializers import PokemonSerializer
from .tasks import fetch_all_pokemons


class PokemonViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para el modelo Pokémon
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class FetchAllPokemonsJobView(APIView):
    """
    Vista para ejecutar el job que extrae los primeros 150 Pokémon.
    """
    def post(self, request):
        fetch_all_pokemons.delay()  # Llama al job de manera asincrónica
        return Response(
            {"message": "Job para extraer los 150 Pokémon iniciado."},
            status=status.HTTP_202_ACCEPTED
        )
