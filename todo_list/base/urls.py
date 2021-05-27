from django.urls import path
from django.urls.resolvers import URLPattern
from .views import TaskDetail, TaskList, TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
]