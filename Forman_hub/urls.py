from django.urls import path
from . import views

app_name='foreman_hub'

urlpatterns = [
    path('', views.foreman_main, name='foreman_main'),
    path('pdf/', views.Pdf.as_view(), name='pdf')
]
