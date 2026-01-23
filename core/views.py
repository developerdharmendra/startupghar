from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    context={
        "hero_images": HeroSectionImage.objects.filter(is_active=True),
    }
    return render(request, "index.html", context=context)