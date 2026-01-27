from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    total_status = Status.objects.all()
    about_us = About.objects.filter(is_active=True)
    services = Service.objects.all()
    patners = Patner.objects.all()
    members = Member.objects.all()
    context={
        "hero_images": HeroSectionImage.objects.filter(is_active=True),
        "total_status": total_status,
        "about_us": about_us,
        "services": services,
        "patners": patners,
        "members": members,
    }
    return render(request, "index.html", context=context)