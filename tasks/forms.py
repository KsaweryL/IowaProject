from django import forms
from .models import Task
import datetime

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'user', 'deadline']