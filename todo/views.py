# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, TodoItem
from .forms import TodoForm, TodoItemForm


def index(request):
    todos = Todo.objects.all()
    return render(request, "todo/index.html", {'todos': todos})

def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, "todo/detail.html", {'todo': todo})

def new_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todo:index')
    else:
        form = TodoForm()
    return render(request, "todo/new.html", {'form': form})

def add_item(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('todo:detail', args=[todo_id])
    else:
        form = TodoItemForm()
    return render(request, "todo/add_item.html", {'todo': todo, 'form': form})

def remove_item(request, todo_id, item_id):
    todo_item = get_object_or_404(TodoItem, pk=item_id, todo__pk=todo_id)
    if request.method == 'POST':
        todo_item.remove()
        return redirect('todo-detail', args=[todo_id])
    return render(request, "todo/remove_item.html", {'todo_item': todo_item})
