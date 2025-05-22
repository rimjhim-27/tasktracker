from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')
    return render(request, 'tasks/add_task.html')

def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('/')
