from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.spaces, name="spaces"),
    path('<int:id>', views.space, name="space")
]