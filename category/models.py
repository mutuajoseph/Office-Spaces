from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):

    category_name = models.CharField(max_length=50)
    category_slug = models.SlugField(max_length=50)
    category_description = models.CharField(max_length=1000)
    category_image = models.ImageField(upload_to="photos/categories")

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('spaces_by_category', args=[self.category_slug])

    def __str__(self) -> str:
        return self.category_name
