from .models import Category


# A function that returns a dict of categories
def categories_list(request):

    categories =  Category.objects.all()
    return dict(links=categories)