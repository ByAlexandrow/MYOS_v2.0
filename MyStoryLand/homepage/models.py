from django.db import models

from tinymce.models import HTMLField


class Photos(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Название',
    )
    image = models.ImageField(
        upload_to='homepage/',
        verbose_name='Титульные картинки',
    )
    description = HTMLField(
        verbose_name='Описание категории'
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
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
