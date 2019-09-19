from django.urls import path
from django.conf.urls import url
from . import views

app_name='foreman_hub'

urlpatterns = [
    path('', views.foreman_main, name='foreman_main'),
    path('pdf/', views.Pdf.as_view(), name='pdf'),
    path('<str:requested_location>/', views.foreman_main, name='foreman_main'),
    path('<str:requested_location>/<str:options>', views.foreman_main, name='foreman_main'),
]
