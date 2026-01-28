from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    total_status = Status.objects.all()
    about_us = About.objects.filter(is_active=True)
    services = Service.objects.all()
    patners = Patner.objects.all()
    members = Member.objects.all()
    team_members = Team.objects.all()
    testimonials = Testimonial.objects.filter(is_active=True)
    projects = Project.objects.all()
    context={
        "hero_images": HeroSection.objects.filter(is_active=True),
        "total_status": total_status,
        "about_us": about_us,
        "services": services,
        "patners": patners,
        "members": members,
        "team_members": team_members,
        "testimonials": testimonials,
        "projects": projects,
    }
    return render(request, "index.html", context=context)

def project_detail(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    context = {
        "project": project,
    }
    return render(request, "project_detail.html", context=context)

def privacy_policy(request):
    return render(request, "privacy_policy.html")
