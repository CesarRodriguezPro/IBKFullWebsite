from django.urls import path
from . import views
app_name = 'dailyTrainingLog'

urlpatterns = [
    path("pdf/",views.dailyTrainigLog_pdf, name="dailyTrainingLog_pdf"),
]
