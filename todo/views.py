from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    try:
        items = TodoItem.objects.all()
        return render(request, 'todo/todo_list.html', {'items': items})
    except Exception as e:
        print(f"Error: {e}")  # This will help log the error to the console
        return render(request, 'todo/error.html')  # You can create a simple error template


def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        TodoItem.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'todo/add_todo.html')  # Ensure this points to the right template

