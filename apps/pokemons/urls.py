from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, FetchAllPokemonsJobView

# Crear un enrutador para el CRUD
router = DefaultRouter()
router.register(r'', PokemonViewSet, basename='pokemon')

urlpatterns = [
    # Rutas del CRUD de Pokémon
    path('', include(router.urls)),
    # Ruta para ejecutar el job
    path('job/fetch-all/', FetchAllPokemonsJobView.as_view(), name='fetch-all-pokemons-job'),
]
