import pytest
from django.core.exceptions import ValidationError

from api.inventions.models import Invention


@pytest.mark.django_db
def test_invention_creation(test_invention):
    """Проверка создания модели."""
    assert test_invention.title_name == 'Test Invention'
    assert test_invention.title_img == 'test/path/to/title_img.png'
    assert test_invention.title_description == 'Test Description'
    assert test_invention.audio == 'test/path/to/audio.mp3'
    assert test_invention.tag_color == '#FF0000'
    assert test_invention.is_published is True
    assert test_invention.created_at is not None


@pytest.mark.django_db
def test_invention_str_method(test_invention):
    """Проверка работы метода __str__."""
    assert str(test_invention) == 'Test Invention'


@pytest.mark.django_db
def test_invention_ordering(test_superuser):
    """Проверка сортировки по умолчанию."""
    invention_1 = Invention.objects.create(
        title_name='Invention 1',
        title_description='Description 1',
        author=test_superuser
    )
    invention_2 = Invention.objects.create(
        title_name='Invention 2',
        title_description='Description 2',
        author=test_superuser
    )
    inventions = Invention.objects.all()
    assert inventions[0] == invention_2
    assert inventions[1] == invention_1


@pytest.mark.django_db
def test_invention_name_max_len_validation(test_superuser):
    """Проверка максимальной длины поля name (30 символов)."""
    with pytest.raises(ValidationError):
        invention = Invention.objects.create(
            title_name='A' * 31,
            title_description='Too many symbols in the title_name field',
            author=test_superuser
        )
        invention.full_clean()


@pytest.mark.django_db
def test_invention_description_max_len_validation(test_superuser):
    """Проверка максимальной длины поля description (50 символов)."""
    with pytest.raises(ValidationError):
        invention = Invention.objects.create(
            title_name='Test Invention',
            title_description='A' * 51,
            author=test_superuser
        )
        invention.full_clean()


@pytest.mark.django_db
def test_invention_default_values(test_superuser):
    """Проверка значений по умолчанию."""
    invention = Invention.objects.create(
        title_name='Default Test Invention',
        title_description='Default Test Description',
        author=test_superuser
    )
    assert invention.tag_color == '#000000'
    assert invention.is_published is False
