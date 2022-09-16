from .models import Blog
from django.forms import ModelForm, TextInput, Textarea


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
