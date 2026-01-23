from django.db import models

# Create your models here.

class HeroSectionImage(models.Model):
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