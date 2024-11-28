from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AbilityViewSet

router = DefaultRouter()
router.register('', AbilityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
