from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')


@login_required()
def redirect_to(request):
    if request.user.groups.filter(name='SystemAdmin').exists():
        request.session['type'] = 'SystemAdmin'
        return HttpResponseRedirect(reverse('foreman_hub:foreman_main'))

    elif request.user.groups.filter(name='Foreman').exists():
        request.session['type'] = 'Foreman'
        return HttpResponseRedirect(reverse('foreman_hub:foreman_main'))

    elif request.user.groups.filter(name='office').exists():
        request.session['type'] = 'office'
        return HttpResponseRedirect(reverse('foreman_hub:foreman_main'))

    elif request.user.groups.filter(name='Employees').exists():
        request.session['type'] = 'Employees'
        return HttpResponseRedirect(reverse('employees:Hub'))

    else:
        return HttpResponseRedirect(reverse('home'))
