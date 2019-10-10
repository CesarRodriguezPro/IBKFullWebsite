from django.urls import path
from django.conf.urls import url
from . import views

app_name='foreman_hub'

urlpatterns = [
    path('', views.main_hub, name='foreman_main'),
    path('<str:requested_location>/', views.main_hub, name='foreman_main'),
    path('<str:requested_location>/<str:options>', views.main_hub, name='foreman_main'),
]
