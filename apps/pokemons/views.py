from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pokemon
from .serializers import PokemonSerializer
from .tasks import fetch_all_pokemons
from .pagination import CustomPokemonPagination  # Importar el paginador personalizado
from .permissions import AllowGetWithoutAuthentication  # Importar el permiso personalizado


class PokemonViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para el modelo Pokémon
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    pagination_class = CustomPokemonPagination  # Usar el paginador personalizado
    permission_classes = [AllowGetWithoutAuthentication]  # Aplicar el permiso personalizado


class FetchAllPokemonsJobView(APIView):
    """
    Vista para ejecutar el job que extrae los primeros 150 Pokémon.
    """
    permission_classes = [AllowGetWithoutAuthentication]  # Opcional, si quieres que GET también sea público
    def post(self, request):
        fetch_all_pokemons.delay()  # Llama al job de manera asincrónica
        return Response(
            {"message": "Job para extraer los 150 Pokémon iniciado."},
            status=status.HTTP_202_ACCEPTED
        )
