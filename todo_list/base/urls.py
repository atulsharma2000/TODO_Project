from django.urls import path
from .views import tasklist

urlpatterns = [
    path('', tasklist, name='tasks'),
]