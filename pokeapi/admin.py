from django.contrib import admin
from .models import Pokemon, Ability

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'types', 'weight', 'abilities', 'image_front', 'image_back')
    search_fields = ('name', 'types', 'abilities')

@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'short_effect')
    search_fields = ('name',)
