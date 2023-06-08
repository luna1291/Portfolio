from .models import Projects
from django.forms import ModelForm, TextInput, Textarea

class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'short_disc', 'text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название проекта'
            }),
            'short_disc': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание проекта'
            }),
        }