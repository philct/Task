from django.shortcuts import render, redirect
from django.http import request
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    return render(request, "tasks/task_list.html")

def add_task(request):
    form = NewTaskForm()
    return render(request, "tasks/add_task.html", 
                  {
                    'form': form
                  },
                )