from django.urls import path
from . import views
app_name = 'downloadDocuments'

urlpatterns = [
    path('',views.list_view.as_view())
]
