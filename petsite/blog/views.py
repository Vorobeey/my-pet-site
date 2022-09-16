from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog


def index(request):
    blogs = Blog.objects.order_by('id')[:1]
    return render(request, 'blog/index.html', {'title': 'Главная страница сайта', 'blogs': blogs})
