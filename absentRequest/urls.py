from django.urls import path
from . import views

app_name='absentRequest'

urlpatterns = [
    path('', views.absent_request, name='absent_request'),
    path('viewinfo', views.absent_viewinfo, name='absent_viewinfo'),
]