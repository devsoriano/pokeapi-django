from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pokemons/', include('apps.pokemons.urls')),
    path('api/abilities/', include('apps.abilities.urls')),
]
