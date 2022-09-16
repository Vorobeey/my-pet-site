from django.shortcuts import render
from .models import Blog


def index(request):
    blog1 = Blog.objects.all()[:1]
    blog2 = Blog.objects.all()[1:2]
    blog3 = Blog.objects.all()[2:3]
    return render(request, 'blog/index.html', {'title': 'Главная страница сайта', 'blog1': blog1,
                                               'blog2': blog2, 'blog3': blog3})


def create(request):
    return render(request, 'blog/create.html')