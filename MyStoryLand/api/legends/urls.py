from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LegendViewSet


router = DefaultRouter()
router.register(r'legends', LegendViewSet, basename='legend')

urlpatterns = [
    path('', include(router.urls)),
]
