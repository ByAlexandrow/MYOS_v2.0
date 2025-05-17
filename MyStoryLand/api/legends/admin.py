from django.contrib import admin
from django.db import models

from api.legends.models import Legend
from tinymce.widgets import TinyMCE


@admin.register(Legend)
class LegendAdmin(admin.ModelAdmin):
    list_display = ('title_name', 'tag_color', 'author', 'is_published')
    list_filter = ('is_published', 'created_at', 'author')
    search_fields = ('title_name', 'author__username', 'is_published')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 50})},
    }
