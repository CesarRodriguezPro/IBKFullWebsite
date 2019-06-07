from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import template
from . import itcontrol

register = template.Library()

# Create your views here.
@login_required

def foreman_main(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    active = itcontrol.ItControl(first_name=first_name, last_name=last_name)
    current_not, primary_not = active.check_function()

    data = {
        'current_employees': active.current_employees_count(),
        'list_of_devices': active.list_of_devices(),
        'warning_not_today_clock_in': active.warning_not_today_clock_in,
        'current_not': current_not,
        'primary_not': primary_not,
     }
    return render(request, 'forman_hub/main.html', context=data)


@login_required
def system_admin(request):

    first_name = request.user.first_name
    last_name = request.user.last_name
    active = itcontrol.ItControl(first_name=first_name, last_name=last_name)

    locations = {'locations': ''}
    current_not, primary_not = active.check_function()
    data = {
        'current_employees': active.current_employees_count(),
        'list_of_devices': active.list_of_devices(),
        'warning_not_today_clock_in': active.warning_not_today_clock_in,
        'current_not': current_not,
        'primary_not': primary_not,
        'locations':locations,
     }
    return render(request, 'forman_hub/SystemAdmin.html', context=data)
