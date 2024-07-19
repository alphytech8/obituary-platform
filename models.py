from django.db import models

# Create your models here.

from django.db import models

class Obituary(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    death_date = models.DateField()
    biography = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    seo_title = models.CharField(max_length=255)
    seo_description = models.TextField()
    social_media_tags = models.TextField()

    def __str__(self):
        return self.name
