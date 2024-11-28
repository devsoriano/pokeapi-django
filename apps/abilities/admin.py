from django.contrib import admin
from .models import Ability

@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    # Muestra los atributos actuales del modelo Ability
    list_display = ("id", "name", "description", "short_effect")
    search_fields = ("name", "description", "short_effect")
