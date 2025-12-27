from django.shortcuts import render, redirect
from django.http import request

# Create your views here.
def index(request):
    if 'tasks' not in request.session['tasks']:
        request.session['tasks'] = []

    return render(request, "tasks/task_list.html")
