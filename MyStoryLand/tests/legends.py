import pytest
from django.core.exceptions import ValidationError

from api.legends.models import Legend


@pytest.mark.django_db
def test_legend_creation(test_legend):
    """"."""
    assert test_legend.title_name == 'Test Legend'
    assert test_legend.title_img == 'test/path/to/title_img.png'
    assert test_legend.title_description == 'Test Description'
    assert test_legend.tag_color == '#FF0000'
    assert test_legend.is_published is True
    assert test_legend.created_at is not None


@pytest.mark.django_db
def test_legend_str_method(test_legend):
    """."""
    assert str(test_legend) == 'Test Legend'


@pytest.mark.django_db
def test_legend_ordering(test_user):
    """."""
    legend_1 = Legend.objects.create(
        title_name='Legend 1',
        title_description='Description 1',
        author=test_user
    )
    legend_2 = Legend.objects.create(
        title_name='Legend 2',
        title_description='Description 2',
        author=test_user
    )
    legends = Legend.objects.all()
    assert legends[0] == legend_2
    assert legends[1] == legend_1


@pytest.mark.django_db
def test_legend_name_max_len_validation(test_user):
    """."""
    with pytest.raises(ValidationError):
        legend = Legend.objects.create(
            title_name='A' * 31,
            title_description='Too many symbols in the title_name field',
            author=test_user
        )
        legend.full_clean()


@pytest.mark.django_db
def test_legend_description_max_len_validation(test_user):
    """."""
    with pytest.raises(ValidationError):
        legend = Legend.objects.create(
            title_name='Test Legend',
            title_description='A' * 51,
            author=test_user
        )
        legend.full_clean()


@pytest.mark.django_db
def test_legend_default_values(test_legend, test_user):
    """."""
    assert test_legend.tag_color == '#FF0000'
    assert test_legend.is_published is False
