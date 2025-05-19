from rest_framework import viewsets

from api.inventions.models import Invention
from api.inventions.serializers import InventionSerializer


class InventionViewSet(viewsets.ModelViewSet):
    queryset = Invention.objects.all().order_by('-created_at')
    serializer_class = InventionSerializer
