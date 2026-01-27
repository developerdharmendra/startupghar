from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.db import models
# Register your models here.
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import ChoicesDropdownFilter
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

@admin.register(HeroSectionImage)
class HeroSectionImageAdmin(ModelAdmin):
    list_display = ("sub_title","title","description", "display_image")  # show preview in list view

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="80" />', obj.image.url)
        return "-"

    display_image.short_description = "Preview"

@admin.register(Status)
class StatusAdmin(ModelAdmin):
    list_display = ("name", "status_number")
    search_fields = ("name", "status_number")
    list_filter = (
        ("status_number", ChoicesDropdownFilter),
    )

@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = (
        "title",
        "description",
        "short_description",
        "display_image_back",
        "display_image_front",
        "is_active",
    )

    def display_image_back(self, obj):
        if obj.image_back:
            return format_html('<img src="{}" width="80" />', obj.image_back.url)
        return "-"

    def display_image_front(self, obj):
        if obj.image_front:
            return format_html('<img src="{}" width="80" />', obj.image_front.url)
        return "-"

    display_image_back.short_description = "Back Image"
    display_image_front.short_description = "Front Image"

@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = (
        "title",
        "description",
        "display_image",
    )

    def display_image(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="80" />', obj.icon.url)
        return "-"

    display_image.short_description = "Icon Preview"

@admin.register(Patner)
class PatnerAdmin(ModelAdmin):
    list_display = (
        "name",
        "link",
        "display_logo",
    )

    def display_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="80" />', obj.logo.url)
        return "-"

    display_logo.short_description = "Logo Preview"

@admin.register(Member)
class MemberAdmin(ModelAdmin):
    list_display = (
        "name",
        "address",
        "phone_number",
        "position",
        "company_name",
        "display_photo",
    )

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="80" />', obj.photo.url)
        return "-"

    display_photo.short_description = "Photo Preview"

@admin.register(Team)
class TeamAdmin(ModelAdmin):
    list_display = (
        "name",
        "position",
        "display_photo",
    )

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="80" />', obj.photo.url)
        return "-"

    display_photo.short_description = "Photo Preview"

@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = (
        "client_name",
        "profession",
        "rating",
        "display_image",
        "is_active",
    )
    list_filter = ("rating", "is_active")
    search_fields = ("client_name", "profession")

    def display_image(self, obj):
        if obj.client_image:
            return format_html('<img src="{}" width="80" />', obj.client_image.url)
        return "-"

    display_image.short_description = "Client Image"




