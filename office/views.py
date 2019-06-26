from django.shortcuts import render
from django.http import HttpResponse
from Forman_hub import FuntionRoot


def main_view(request):


    return render(request, 'office/main.html')
    