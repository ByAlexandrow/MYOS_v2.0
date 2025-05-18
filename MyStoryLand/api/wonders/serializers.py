from rest_framework import serializers

from api.wonders.models import Wonder


class WonderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wonder
        fields = [
            'id', 'title_name', 'title_img', 'title_description',
            'audio', 'tag_color', 'author', 'created_at', 'is_published'
        ]
        read_only_fields = ['id', 'created_at']
