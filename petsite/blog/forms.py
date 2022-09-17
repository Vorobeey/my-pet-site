from .models import *
from django.forms import ModelForm, TextInput, Textarea, ImageField, FileInput, ClearableFileInput


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'photo']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            'photo': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Изображение'
            })
        }
