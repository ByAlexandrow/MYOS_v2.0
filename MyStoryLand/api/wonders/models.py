from django.db import models
from django.contrib.auth import get_user_model

from tinymce.models import HTMLField


User = get_user_model()


class Wonder(models.Model):
    title_name = models.CharField(
        max_length=30,
        verbose_name='Название статьи',
        db_index=True,
    )
    title_img = models.ImageField(
        upload_to='wonders/title_img/',
        verbose_name='Титульное изображение',
    )
    title_description = models.CharField(
        max_length=50,
        verbose_name='Описание',
        null=False,
    )
    content = HTMLField(
        verbose_name='Содержание',
        blank=True,
    )
    tag_color = models.CharField(
        max_length=7,
        verbose_name='Tag',
        default='#000000',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Автор',
        db_index=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        db_index=True,
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовать',
        db_index=True,
    )

    def __str__(self):
        return self.title_name
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Чудо'
        verbose_name_plural = 'Чудеса'
