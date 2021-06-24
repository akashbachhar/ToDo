from django import forms
from django.forms import ModelForm
from .models import Todo


class ToDoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['todo']
        widgets = {
            'todo': forms.TextInput(attrs={'class': 'form-control', 'id': 'taskid', 'placeholder': 'New Task'}),
        }
