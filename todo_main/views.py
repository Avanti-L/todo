# from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Task


def home(request):
    # Use '-updated_at' for descending order and 'updated_at' for ascending order
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at') 
    context = {
        'tasks': tasks
    }
    return render(request, 'home.html', context)