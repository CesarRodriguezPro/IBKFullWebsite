from django.shortcuts import render
from DrawingsTrackerApp.models import Drawings


def home(request):
    return render(request, 'controlapp/home.html',{})


def check_drawings_request(request, code):
    drawings = Drawings.objects.get(code_Id=code)
    return render(request, 'DrawingsTracker/test.html', context={'message': drawings})
