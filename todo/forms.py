from django import forms
from .models import Task, Category


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
