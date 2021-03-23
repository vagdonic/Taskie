from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# Create your views here.
def defacto(request):
    tasks = Task.objects.all
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}

    return render(request, 'taskie/tasks.html', context)

def updateTask(request, pkey):
    task = Task.objects.get(id = pkey)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'taskie/update_task.html', context)

def deleteTask(request, pkey):
    task = Task.objects.get(id = pkey)

    if request.method == 'POST':
        task.delete()
        return redirect('/')
    
    context = {'task': task}
    return render(request, 'taskie/del.html', context)