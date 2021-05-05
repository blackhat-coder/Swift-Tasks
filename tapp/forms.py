from django.forms import ModelForm
from django import forms
from .models import TodoModel

class taskform(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'body']