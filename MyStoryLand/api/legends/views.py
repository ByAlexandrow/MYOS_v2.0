from rest_framework import viewsets

from api.legends.models import Legend
from api.legends.serializers import LegendSerializer


class LegendViewSet(viewsets.ModelViewSet):
    queryset = Legend.objects.all().order_by('-created_at')
    serializer_class = LegendSerializer
