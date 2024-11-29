from rest_framework.permissions import BasePermission, SAFE_METHODS

class AllowGetWithoutAuthentication(BasePermission):
    """
    Permite solicitudes GET sin autenticación.
    Otros métodos requieren autenticación.
    """
    def has_permission(self, request, view):
        # Permitir GET sin autenticación
        if request.method in SAFE_METHODS:  # SAFE_METHODS incluye GET, HEAD, OPTIONS
            return True
        # Requiere autenticación para otros métodos
        return request.user and request.user.is_authenticated
