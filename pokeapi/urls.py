from django.contrib import admin
from django.urls import path
from .views import run_job, get_pokemons, get_abilities

urlpatterns = [
    path('admin/', admin.site.urls),
    path('run-job/', run_job, name='run_job'),
    path('get-pokemons/', get_pokemons, name='get_pokemons'),
    path('get-abilities/', get_abilities, name='get_abilities'),
]
