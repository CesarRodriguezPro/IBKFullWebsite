from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.EmployeeMainView.as_view()),
    path('create/', views.EmployeeCreateView.as_view()),
    path('listview/', views.EmployeeCreateView.as_view()),
    path('detailview/', views.EmployeeCreateView.as_view()),
    path('update/', views.EmployeeCreateView.as_view()),
    path('delete/', views.EmployeeCreateView.as_view()),
]



