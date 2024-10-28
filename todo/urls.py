from django.urls import path
from .views import todo_list, add_todo

urlpatterns = [
    path('', todo_list, name='todo_list'),  # This should be your main list view
    path('add/', add_todo, name='add_todo'),
]
