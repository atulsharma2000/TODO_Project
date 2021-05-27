from django.shortcuts import redirect, render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy           #redirects user to certain page
from .models import Task

from django.contrib.auth.mixins import LoginRequiredMixin   #setting up the restrictions
                            #add the mixin before the Listview itself 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login         #for instant login after registration

# Create your views here.

class TaskList(LoginRequiredMixin, ListView):       #now view is restricted
    model = Task                # this looks for task_list.html
    context_object_name = 'tasks'       #giving custom name to query set (that was object_list in html)
    
    def get_context_data(self, **kwargs):                   #making user-specific data
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task                #looks for task_detail.html
    context_object_name = 'task'
    template_name = 'base/task.html'  #customizing the deafult task_detail.html to task.html or other


class TaskCreate(LoginRequiredMixin, CreateView):#looks for base/task_form.html
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')    #passing the url name 'tasks'

    def form_valid(self, form):                         #for user specific input (no other user option)
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task                     #this view also looks for base/task_form.html
    fields = ['title', 'description', 'complete']     
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


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):      #redirect_authenticated_user = True wasnt helpfull so our own
        if self.request.user.is_authenticated:
            return redirect(task)
        return super(RegisterPage, self).get(*args, **kwargs)