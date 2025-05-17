from rest_framework import serializers

from api.legends.models import Legend


class LegendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legend
        fields = [
            'id', 'title_name', 'title_img', 'title_description',
            'tag_color', 'author', 'created_at', 'is_published'
        ]
        read_only_fields = ['id', 'created_at']
