from django import forms
from .models import Todo, TodoItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('name',)

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ('todo', 'text',)
