from django.shortcuts import render
# from .models import Category, Item


def index(request):
    # tasks = Category.objects.all()
    return render(request, 'core/index.html')  # {'title': 'Main page', 'tasks': tasks}


def about(request):
    return render(request, 'core/about.html')


def why(request):
    return render(request, 'core/why.html')