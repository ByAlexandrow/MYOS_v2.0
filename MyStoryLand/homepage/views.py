from django.shortcuts import render
from django.views.decorators.cache import cache_page

from homepage.models import Photos


# @cache_page(60 * 15)
def index(request):
    photos = Photos.objects.all()
    return render(request, 'homepage/index.html', {'photos': photos})
