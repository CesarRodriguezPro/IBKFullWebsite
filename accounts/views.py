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

            if user.is_active and user.groups.filter(name='SystemAdmin').exists():
                login(request, user)
                request.session['type'] = 'systemAdmin'
                return HttpResponseRedirect(reverse('foreman_hub:foreman_main'))

            elif user.is_active and user.groups.filter(name='Foreman').exists():
                login(request, user)
                request.session['type'] = 'foreman'
                return HttpResponseRedirect(reverse('foreman_hub:foreman_main'))

            elif user.is_active and user.groups.filter(name='office').exists():
                login(request, user)
                request.session['type'] = 'office'
                return HttpResponseRedirect(reverse('office:main_view'))

            elif user.is_active:
                login(request, user)
                request.session['type'] = 'normal'
                return HttpResponseRedirect(reverse('home'))

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
