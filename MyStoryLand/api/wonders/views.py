from rest_framework import viewsets

from api.wonders.models import Wonder
from api.wonders.serializers import WonderSerializer


class WonderViewSet(viewsets.ModelViewSet):
    queryset = Wonder.objects.all().order_by('-created_at')
    serializer_class = WonderSerializer
