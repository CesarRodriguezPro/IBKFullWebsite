"""Drawings Tracker URL Configuration"""

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'drawings_app'

urlpatterns = [
    path('', views.drawings_main, name='drawings_main'),
    path('add/', views.drawings_add, name='drawings_add'),
    path('viewinfo/', views.drawings_viewinfo, name='drawings_viewinfo'),
    path('delete/', views.drawings_delete, name='drawings_delete'),
]
