from django.db import models
from django.utils.text import slugify
# Create your models here.

class HeroSection(models.Model):
    sub_title = models.CharField(max_length=155)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="hero/")
    alt_name = models.CharField(max_length=155)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = "herosection"

    def __str__(self):
        return self.alt_name

class Status(models.Model):
    name = models.CharField(max_length=100)
    status_number = models.IntegerField()

    class Meta:
        db_table = "status"

    def __str__(self):
        return self.name

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    short_description = models.TextField()
    image_back = models.ImageField(upload_to="about/")
    image_front = models.ImageField(upload_to="about/")
    alt_name = models.CharField(max_length=155)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = "about"

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to="services/")
    alt_name = models.CharField(max_length=155)

    class Meta:
        db_table = "service"

    def __str__(self):
        return self.title
    
class Patner(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    logo = models.ImageField(upload_to="patners/")
    alt_name = models.CharField(max_length=155)

    class Meta:
        db_table = "patner"

    def __str__(self):
        return self.name
    
class Member(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="members/")
    alt_name = models.CharField(max_length=155)

    class Meta:
        db_table = "member"

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="teams/")
    alt_name = models.CharField(max_length=155)

    class Meta:
        db_table = "team"

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    testimonial_text = models.TextField()
    client_image = models.ImageField(upload_to="testimonials/")
    alt_name = models.CharField(max_length=155)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "testimonial"

    def __str__(self):
        return f"{self.client_name} - {self.profession}"

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    alt_name = models.CharField(max_length=155)

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)