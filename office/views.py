from django.shortcuts import render
from django.http import HttpResponse


def main_view(request):
    return render(request, 'office/main.html')
    