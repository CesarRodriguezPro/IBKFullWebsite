from django.contrib import admin
from django.urls import path
from . import views

app_name='vacationRequest'

urlpatterns = [
    path('', views.vacation_request, name='vacation_request'),
    path('viewinfo', views.vacation_viewinfo, name='vacation_viewinfo'),
    path('render/pdf/', views.pdf_resource, name='pdf_resource'),
]