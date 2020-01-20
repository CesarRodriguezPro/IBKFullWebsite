from django.urls import path
from . import views

app_name = 'uploadExcel'
urlpatterns = [
    path('', views.upload, name='upload')
]