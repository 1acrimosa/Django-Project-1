from django.shortcuts import render
from item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })  # {'title': 'Main page', 'tasks': tasks}


def about(request):
    return render(request, 'core/about.html')


def why(request):
    return render(request, 'core/why.html')
