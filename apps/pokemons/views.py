from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pokemon
from .serializers import PokemonSerializer
from .tasks import fetch_all_pokemons
from .pagination import CustomPokemonPagination
from .permissions import AllowGetWithoutAuthentication


class PokemonViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para el modelo Pokémon
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    pagination_class = CustomPokemonPagination
    permission_classes = [AllowGetWithoutAuthentication]


class FetchAllPokemonsJobView(APIView):
    """
    Vista para ejecutar el job de extracción de Pokémon con rangos de páginas.
    """

    def post(self, request):
        start_page = request.data.get('start_page', 1)
        end_page = request.data.get('end_page', 1)

        try:
            # Convertir los parámetros a enteros
            start_page = int(start_page)
            end_page = int(end_page)

            # Validaciones
            if start_page <= 0 or end_page <= 0:
                return Response(
                    {"error": "start_page and end_page must be positive integers."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if start_page > end_page:
                return Response(
                    {"error": "start_page cannot be greater than end_page."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Llamar al job de Celery
            fetch_all_pokemons.delay(start_page=start_page, end_page=end_page)

            return Response(
                {"message": f"Fetching Pokémon data from pages {start_page} to {end_page} initiated."},
                status=status.HTTP_200_OK,
            )

        except ValueError:
            return Response(
                {"error": "Invalid start_page or end_page values. They must be integers."},
                status=status.HTTP_400_BAD_REQUEST,
            )