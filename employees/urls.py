from django.urls import path, include
from . import views


app_name = 'employees'

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('timesheet/', views.EmployeesHub.as_view(), name='Hub'),
    path('hourChange/',views.hour_change, name='HoursChange'),

]