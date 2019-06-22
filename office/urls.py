

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name='office'

urlpatterns = [
    path('', views.main_view, name = 'main_view'),
]
