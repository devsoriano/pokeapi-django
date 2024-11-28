from django.contrib import admin
from .models import Ability

@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "short_effect")
    search_fields = ("name", "description", "short_effect")
