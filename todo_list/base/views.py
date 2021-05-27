from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy           #redirects user to certain page

from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task                # this looks for task_list.html
    context_object_name = 'tasks'       #giving custom name to query set (that was object_list in html)


class TaskDetail(DetailView):
    model = Task                #looks for task_detail.html
    context_object_name = 'task'
    template_name = 'base/task.html'  #customizing the deafult task_detail.html to task.html or other


class TaskCreate(CreateView):#looks for base/task_form.html
    model = Task
    fields = '__all__'      #making all fields['title', 'description']
    success_url = reverse_lazy('tasks')    #passing the url name 'tasks'