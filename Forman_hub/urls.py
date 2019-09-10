from django.urls import path
from django.conf.urls import url
from . import views

app_name='foreman_hub'

urlpatterns = [
    path('', views.foreman_main, name='foreman_main'),
    path('pdf/', views.Pdf.as_view(), name='pdf'),
    path('<str:request_locations>/', views.foreman_main, name='foreman_main'),
]
