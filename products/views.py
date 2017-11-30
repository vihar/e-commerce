from django.shortcuts import get_object_or_404, render

from .models import Categorie, Item

# Create your views here.


def home_view(request):
    categories = Categorie.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context)


def categorie_view(request):
    categories = Categorie.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)


def all_items_view(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'items.html', context)


def categorie_detail(request):
    categorie = get_object_or_404(Categorie)
    items = Item.objects.filter(categorie=categorie)
    context = {
        'categorie': categorie,
        'items': items
    }
    return render(request, 'item_filter.html', context)
