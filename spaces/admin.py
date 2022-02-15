from django.contrib import admin
from .models import Space

# Register your models here.
class SpaceAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('space_name',)}
    list_display = ('space_name', 'slug')

admin.site.register(Space, SpaceAdmin)