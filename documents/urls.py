from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'documents'

urlpatterns = [
    path('', views.ListDocument.as_view(), name='list_documents'),
    path('upload/', views.model_form_upload, name='upload'),
    path('delete/<int:pk>', views.delete_document, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)