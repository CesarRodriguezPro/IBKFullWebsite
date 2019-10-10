from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('redirect_to'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            return HttpResponse('<h1>Wrong Password</h1>')
    else:
        return render(request, 'accounts/login.html')


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def registration_user(request):
    form = forms.RegistrationUser()
    if request.method == 'POST':
        form.save()
    return render(request, 'accounts/registration.html', context={'form':form})
