from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.spaces, name="spaces"),
    path('<slug:category_slug>/', views.spaces, name="spaces_by_category"),
    path('<slug:category_slug>/<slug:space_slug>/', views.space, name="space_detail")
]