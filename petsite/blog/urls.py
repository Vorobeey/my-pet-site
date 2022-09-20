from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('create', views.create, name='create'),
	path('contacts', views.contacts, name='contacts'),
	path('about_me', views.about_me, name='about_me'),
]