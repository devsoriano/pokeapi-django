from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import fetch_all_pokemons

class FetchAllPokemonsJobView(APIView):
    def post(self, request):
        fetch_all_pokemons.delay()
        return Response(
            {"message": "Job para extraer los 150 Pokémon iniciado."},
            status=status.HTTP_202_ACCEPTED
        )
