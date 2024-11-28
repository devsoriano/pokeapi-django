from django.urls import path
from .views import FetchAllPokemonsJobView

urlpatterns = [
    path('job/fetch-all/', FetchAllPokemonsJobView.as_view(), name='fetch-all-pokemons-job'),
]
