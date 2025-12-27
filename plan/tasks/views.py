from django.shortcuts import render, redirect
from django.http import request
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []
        
    return render(request, "tasks/task_list.html", { 'tasks': request.session['tasks'] })

def add_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            update_task = request.session['tasks']
            update_task.append(task)
            request.session['tasks'] = update_task
            return redirect("tasks:index")
        else:
            return render(request, "tasks/add_task.html", { 'form': form })

    return render(request, "tasks/add_task.html", 
                  {
                    'form': NewTaskForm(),
                  },
                )
