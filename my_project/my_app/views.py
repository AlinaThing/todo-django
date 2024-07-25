from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoItems
from .forms import TodoForm, DeleteTodoForm
from django.utils import timezone

def Todolists(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TodoForm()

    todo_items = TodoItems.objects.all()
    return render(request, 'main.html', {'form': form, 'todo_items': todo_items})

def success(request):
    return render(request, 'success.html')

def EditTodoItem(request, pk):
    todo_item = get_object_or_404(TodoItems, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('Todolists')
    else:
        form = TodoForm(instance=todo_item)
    return render(request, 'edit.html', {'form': form, 'todo_item': todo_item})

def DeleteTodoItem(request, pk):
    todo_item = get_object_or_404(TodoItems, pk=pk)
    if request.method == 'POST':
        form = DeleteTodoForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            todo_item.delete()
            return redirect('Todolists')
    else:
        form = DeleteTodoForm()
    return render(request, 'delete.html', {'form': form, 'todo_item': todo_item})
