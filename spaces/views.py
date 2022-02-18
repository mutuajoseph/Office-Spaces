from unicodedata import category
from django.shortcuts import render, get_object_or_404

from category.models import Category
from .models import Space

# Create your views here.

def spaces(request, category_slug=None):

    category = None
    spaces = None

    # check if category is empty 
    if category_slug != None:
        category = get_object_or_404(Category, category_slug=category_slug)
        spaces = Space.objects.filter(category=category)
    else:
        # fetch all the spaces
        spaces = Space.objects.all()

    context = {
        "spaces": spaces
    }

    return render(request, 'spaces.html', context=context)

def space(request, category_slug, space_slug):

    try:
        space = Space.objects.get(category__category_slug=category_slug, space_slug=space_slug)
    except Exception as e:
        raise e
    
    context = {
        "space" : space 
    }

    return render(request, 'space.html', context=context)
