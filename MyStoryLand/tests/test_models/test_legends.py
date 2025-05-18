import pytest
from django.core.exceptions import ValidationError

from api.legends.models import Legend


@pytest.mark.django_db
def test_legend_creation(test_legend):
    """"Проверка создания объекта модели."""
    assert test_legend.title_name == 'Test Legend'
    assert test_legend.title_img == 'test/path/to/title_img.png'
    assert test_legend.title_description == 'Test Description'
    assert test_legend.audio == 'test/path/to/audio.mp3'
    assert test_legend.tag_color == '#FF0000'
    assert test_legend.is_published is True
    assert test_legend.created_at is not None


@pytest.mark.django_db
def test_legend_str_method(test_legend):
    """Проверка метода __str__."""
    assert str(test_legend) == 'Test Legend'


@pytest.mark.django_db
def test_legend_ordering(test_superuser):
    """Проверка сортировки по умолчанию."""
    legend_1 = Legend.objects.create(
        title_name='Legend 1',
        title_description='Description 1',
        author=test_superuser
    )
    legend_2 = Legend.objects.create(
        title_name='Legend 2',
        title_description='Description 2',
        author=test_superuser
    )
    legends = Legend.objects.all()
    assert legends[0] == legend_2
    assert legends[1] == legend_1


@pytest.mark.django_db
def test_legend_name_max_len_validation(test_superuser):
    """Проверка максимальной длины title_name (30 символов)."""
    with pytest.raises(ValidationError):
        legend = Legend.objects.create(
            title_name='A' * 31,
            title_description='Too many symbols in the title_name field',
            author=test_superuser
        )
        legend.full_clean()


@pytest.mark.django_db
def test_legend_description_max_len_validation(test_superuser):
    """Проверка максимальной длины title_description (50 символов)."""
    with pytest.raises(ValidationError):
        legend = Legend.objects.create(
            title_name='Test Legend',
            title_description='A' * 51,
            author=test_superuser
        )
        legend.full_clean()


@pytest.mark.django_db
def test_legend_default_values(test_superuser):
    """Проверка значений по умолчанию."""
    legend = Legend.objects.create(
        title_name='Default Test Legend',
        title_description='Default Test Description',
        author=test_superuser
    )
    assert legend.tag_color == '#000000'
    assert legend.is_published is False
