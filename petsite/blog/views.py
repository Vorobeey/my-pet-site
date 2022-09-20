from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog


def index(request):
    blog1 = Blog.objects.order_by('-id')[:1]
    blog2 = Blog.objects.order_by('-id')[1:2]
    blog3 = Blog.objects.order_by('-id')[2:3]
    return render(request, 'blog/index.html', {'title': 'Главная страница сайта', 'blog1': blog1,
                                               'blog2': blog2, 'blog3': blog3})


def create(request):
    error = ''

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = BlogForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'blog/create.html', context)


def contacts(request):
    return render(request, 'blog/contacts.html')


def about_me(request):
    return render(request, 'blog/about_me.html')