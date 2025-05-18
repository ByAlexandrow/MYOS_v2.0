from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WonderViewSet


router = DefaultRouter()
router.register(r'wonder', WonderViewSet, basename='wonder')

urlpatterns = [
    path('', include(router.urls)),
]
