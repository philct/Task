from django.shortcuts import render, redirect
from django.http import request
from django import forms

tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    return render(request, "tasks/task_list.html", { 'tasks': tasks })

def add_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            update_task = task
            tasks.append(update_task)
            return redirect("tasks:add_task")
        else:
            return render(request, "tasks/add_task.html", { 'form': form })

    return render(request, "tasks/add_task.html", 
                  {
                    'form': NewTaskForm(),
                  },
                )
