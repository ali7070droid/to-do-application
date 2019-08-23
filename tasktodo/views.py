from django.shortcuts import render
from .models import Task
from django.utils import timezone
from .forms import TaskForm
from django.http import HttpResponseRedirect

# Create your views here.

def task_list(request):
    tasks = Task.objects.order_by('-created_date')
    return render(request, 'tasktodo/task_list.html', {'tasks': tasks})

def addtodo(request):
    new_item = Task(todo = request.POST['todo'] )
    new_item.author = request.user
    new_item.created_date = timezone.now()
    new_item.save()
    return HttpResponseRedirect('/task_list/')

def deletetodo(request, todo_id):
    del_item = Task.objects.get(id=todo_id)
    del_item.delete()
    return HttpResponseRedirect('/task_list/')
