from django.contrib import admin
from django.db import models

from homepage.models import Photos
from tinymce.widgets import TinyMCE


@admin.register(Photos)
class LegendAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title_name',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 5})},
    }
