from rest_framework import viewsets
from .models import Ability
from .serializers import AbilitySerializer
from .permissions import AllowGetWithoutAuthentication  # Importar el permiso personalizado

class AbilityViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para el modelo Ability
    """
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

    # Deshabilitar la paginación para este ViewSet
    pagination_class = None
    permission_classes = [AllowGetWithoutAuthentication]  # Aplicar el permiso personalizado
