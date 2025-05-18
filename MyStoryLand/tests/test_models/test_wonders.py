import pytest
from django.core.exceptions import ValidationError

from api.wonders.models import Wonder


@pytest.mark.django_db
def test_wonder_creation(test_wonder):
    """Проверка создания объекта модели."""
    assert test_wonder.title_name == 'Test Wonder'
    assert test_wonder.title_img == 'test/path/to/title_img.png'
    assert test_wonder.title_description == 'Test Description'
    assert test_wonder.tag_color == '#FF0000'
    assert test_wonder.is_published is True
    assert test_wonder.created_at is not None


@pytest.mark.django_db
def test_wonder_str_method(test_wonder):
    """Проверка метода __str__."""
    assert str(test_wonder) == 'Test Wonder'


@pytest.mark.django_db
def test_wonder_ordering(test_superuser):
    """Проверка сортировки по умолчанию."""
    wonder_1 = Wonder.objects.create(
        title_name='Wonder 1',
        title_description='Description 1',
        author=test_superuser
    )
    wonder_2 = Wonder.objects.create(
        title_name='Wonder 2',
        title_description='Description 2',
        author=test_superuser
    )
    wonders = Wonder.objects.all()
    assert wonders[0] == wonder_2
    assert wonders[1] == wonder_1


@pytest.mark.django_db
def test_wonder_name_max_len_validation(test_superuser):
    """Проверка максимальной длины title_name (30 символов)."""
    with pytest.raises(ValidationError):
        wonder = Wonder.objects.create(
            title_name='A' * 31,
            title_description='Too many symbols in the title_name field',
            author=test_superuser
        )
        wonder.full_clean()


@pytest.mark.django_db
def test_wonder_description_len_validation(test_superuser):
    """Проверка максимальной длины title_description (50 символов)."""
    with pytest.raises(ValidationError):
        wonder = Wonder.objects.create(
            title_name='Test Wonder',
            title_description='A' * 51,
            author=test_superuser
        )
        wonder.full_clean()


@pytest.mark.django_db
def test_wonder_default_values(test_superuser):
    """Проверка значений по умолчанию."""
    wonder = Wonder.objects.create(
        title_name='Default Test Wonder',
        title_description='Default Test Description',
        author=test_superuser
    )
    assert wonder.tag_color == '#000000'
    assert wonder.is_published is False
