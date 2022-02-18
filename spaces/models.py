from django.urls import reverse
from django.db import models

from category.models import Category

# Create your models here.

class Space(models.Model):

    space_name = models.CharField(max_length=100)
    space_slug = models.SlugField(max_length=100)
    space_description=models.CharField(max_length=1000)
    space_image=models.ImageField(upload_to='photos/spaces', blank=True)
    space_location=models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'space'
        verbose_name_plural = 'spaces'

    def get_url(self):
        return reverse('space_detail', args=[self.category.category_slug, self.space_slug])

    def __str__(self):
        return self.space_name

