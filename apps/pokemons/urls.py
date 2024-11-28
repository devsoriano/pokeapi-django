from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, FetchAllPokemonsJobView

router = DefaultRouter()
router.register('', PokemonViewSet)

urlpatterns = [
    path('job/fetch-all/', FetchAllPokemonsJobView.as_view(), name='fetch-all-pokemons-job'),
    path('', include(router.urls)),
]
