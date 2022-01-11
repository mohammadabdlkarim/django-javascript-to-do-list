from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import List, Task
from .forms import *
import json

def home(request):
    user = request.user
    lists = List.objects.filter(user=user.id)
    return render(request, 'list/home.html', {'lists': lists})

def list_view(request, list_id):
    lst_query = List.objects.filter(id=list_id, user=request.user)
    if lst_query.exists():
        lst = lst_query[0]
        tasks = Task.objects.filter(task_list=lst)
        if request.method == "POST":
            task_form = AddTaskForm(request.POST)
            if task_form.is_valid():
                content = task_form.cleaned_data['task_content']
                done = task_form.cleaned_data['done']
                new_task = Task(content=content, done=done, task_list=lst)
                new_task.save()
                task_form = AddTaskForm()
            else:
                print(task_form.errors)
            return render(request, 'list/list.html', {'list': lst, 'list_tasks': tasks, 'task_form': task_form})
        task_form = AddTaskForm()
        return render(request, 'list/list.html', {'list': lst, 'list_tasks': tasks, 'task_form': task_form})
    return render(request, 'list/list.html')



def change_task_status(task_id):
    payload = {}
    tasks = Task.objects.filter(id=task_id)
    if tasks.exists():
        task = tasks[0]
        if task.done:
            task.done = False
            payload['response'] = "Changed To False"
            print('changed to false')
        else:
            task.done = True
            payload['response'] = "Changed To True"
            print('changed to true')
        task.save()
    else:
        payload['response'] = "Task does not exist"
        print('task doesnot exist')
    return HttpResponse(json.dumps(payload), content_type="application/json")

def change_task_content(request, task_id, content):
    payload = {}
    if request.method == "GET":
        task_id = task_id
        tasks = Task.objects.filter(id=task_id)
        if tasks.exists():
            task = tasks[0]
            task.content = content
            task.save()
            payload['response'] = "Task Updated."
        else:
            payload['response'] = "Task not found."
    return HttpResponse(json.dumps(payload), content_type="application/json")
  
def create_list(request):
    if request.method == "POST":
        f = CreateListForm(request.POST)
        if f.is_valid():
            lst_name = f.cleaned_data['list_name']
            lst = List(name=lst_name, user=request.user)
            lst.save()
            return redirect('/')
        else:
            print(f.errors)
        return render(request, 'list/createList.html', {'form': f})
    f = CreateListForm()
    return render(request, 'list/createList.html', {'form': f})

def delete_list(request, list_id):
    List.objects.filter(id=list_id).delete()
    return redirect('/')

def delete_task(request, task_id):
    task_query = Task.objects.filter(id=task_id)
    if task_query.exists():
        task = task_query[0]
        lst = task.task_list
        task.delete()
        return redirect(f'/{lst.id}')
    return redirect('/')