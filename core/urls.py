from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/<slug:project_slug>/", views.project_detail, name="project_detail"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
]
