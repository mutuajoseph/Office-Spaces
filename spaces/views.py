from django.shortcuts import render
from .models import Space

# Create your views here.

def spaces(request):

    # fetch all the spaces
    spaces = Space.objects.all()

    context = {
        "spaces": spaces
    }

    return render(request, 'spaces.html', context=context)

def space(request, id):

    space = Space.objects.all().filter(id=id)
    
    context = {
        "space" : space 
    }

    return render(request, 'space.html', context=context)
