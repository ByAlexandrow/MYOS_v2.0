import pytest
from django.contrib.auth import get_user_model

from api.legends.models import Legend
from api.wonders.models import Wonder


User = get_user_model()


@pytest.fixture
def test_superuser():
    return User.objects.create_superuser(
        username='Test User',
        email='email@mail.ru',
        password='123123qweqwe',
    )


@pytest.fixture
def test_legend(test_superuser):
    return Legend.objects.create(
        title_name='Test Legend',
        title_img='test/path/to/title_img.png',
        title_description='Test Description',
        content='Test Legend Content',
        audio='test/path/to/audio.mp3',
        tag_color='#FF0000',
        author=test_superuser,
        is_published=True
    )


@pytest.fixture
def test_wonder(test_superuser):
    return Wonder.objects.create(
        title_name='Test Wonder',
        title_img='test/path/to/title_img.png',
        title_description='Test Description',
        content='Test Wonder Content',
        audio='test/path/to/audio.mp3',
        tag_color='#FF0000',
        author=test_superuser,
        is_published=True
    )
