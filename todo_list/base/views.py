from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy           #redirects user to certain page

from .models import Task

from django.contrib.auth.mixins import LoginRequiredMixin   #setting up the restrictions
                            #add the mixin before the Listview itself 


# Create your views here.

class TaskList(LoginRequiredMixin, ListView):       #now view is restricted
    model = Task                # this looks for task_list.html
    context_object_name = 'tasks'       #giving custom name to query set (that was object_list in html)


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task                #looks for task_detail.html
    context_object_name = 'task'
    template_name = 'base/task.html'  #customizing the deafult task_detail.html to task.html or other


class TaskCreate(LoginRequiredMixin, CreateView):#looks for base/task_form.html
    model = Task
    fields = '__all__'      #making all fields['title', 'description']
    success_url = reverse_lazy('tasks')    #passing the url name 'tasks'


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task                     #this view also looks for base/task_form.html
    fields = '__all__'     
    success_url = reverse_lazy('tasks')   


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task                    #lookingg for task_confirm_delete.html
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')   


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')