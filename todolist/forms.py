from django import forms
from django.forms import ModelForm
from . import models
from todolist.models import todo
class TodoListForm(forms.ModelForm):
    class Meta:
        model=todo
        fields='__all__'