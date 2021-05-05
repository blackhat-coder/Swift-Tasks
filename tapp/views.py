from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import TodoModel
from .forms import taskform

def home_view(request):
    tasks = TodoModel.objects.all()
    t_form = taskform()

    if request.method == 'POST':
        t_form = taskform(request.POST)
        if t_form.is_valid():
            t_form.save()
        
        return redirect('/')

    return render(request, 'tapp\index.html', {'tasks':tasks})

def view_todo(request, pk):
    todo = TodoModel.objects.get(id=pk)
    print(todo)
    return render(request, 'tapp/view_todo.html', {'todo':todo})

def delete(request, pk):
    task = TodoModel.objects.get(id=pk)
    task.delete()

    return redirect('/')

def update(request, pk):

    task = TodoModel.objects.get(id=pk)
    t_form = taskform(instance=task)

    if request.method == 'POST':
        t_form = taskform(request.POST, instance=task)
        if t_form.is_valid():
            t_form.save()
        
        return redirect('/')
    
    return render(request, 'tapp/update.html', {'form':t_form, 'task':task})
