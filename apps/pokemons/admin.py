from django.contrib import admin
from .models import Pokemon

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
