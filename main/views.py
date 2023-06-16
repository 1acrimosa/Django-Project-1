from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page of this site', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def why(request):
    return render(request, 'main/why.html')
