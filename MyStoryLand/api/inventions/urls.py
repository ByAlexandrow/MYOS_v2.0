from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import InventionViewSet


router = DefaultRouter()
router.register(r'inventions', InventionViewSet, basename='invention')

urlpatterns = [
    path('', include(router.urls)),
]
