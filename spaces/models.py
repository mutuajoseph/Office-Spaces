from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.forms import CharField, SlugField

# Create your models here.

class Space(models.Model):

    space_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    space_description=models.CharField(max_length=1000)
    space_image=models.ImageField(upload_to='photos/spaces', blank=True)
    space_location=models.CharField(max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.space_name

