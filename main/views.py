from django.shortcuts import render
from .models import Category, Item


def index(request):
    tasks = Category.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def why(request):
    return render(request, 'main/why.html')
