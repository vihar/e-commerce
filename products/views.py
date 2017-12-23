from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import Categorie, Item

# Create your views here.


def home_view(request):
    items = Item.objects.all()[:6]
    context = {
        'items': items
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


class ItemDetail(DetailView):
    model = Item
    template_name = "item.html"
    context_object_name = "item"


def categorie_detail(request, slug):
    categorie = get_object_or_404(Categorie, slug=slug)
    items = Item.objects.filter(categorie=categorie)
    context = {
        'categorie': categorie,
        'items': items
    }
    return render(request, 'item_filter.html', context)


def about_us(request):
    return render(request, 'about.html')


def faqs(request):
    return render(request, 'faqs.html')


def contact(request):
    return render(request, 'contact.html')


def souvenirs(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'souvenirs.html', context)


def pre_boxes(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'pre-boxes.html', context)


def curatedbox(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'curatedbox.html', context)
