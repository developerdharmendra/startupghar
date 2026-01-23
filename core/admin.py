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
