from rest_framework import viewsets
from .models import Ability
from .serializers import AbilitySerializer

class AbilityViewSet(viewsets.ModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
