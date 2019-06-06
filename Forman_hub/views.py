from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import template
from . import itcontrol

register = template.Library()

# Create your views here.
@login_required
def foreman_main(request):

    active = itcontrol.ItControl(request.user)
    current_not, primary_not = active.check_function()

    data = {
        'current_employees': active.current_employees_count(),
        'list_of_devices': active.list_of_devices(),
        'warning_not_today_clock_in': active.warning_not_today_clock_in,
        'current_not': current_not,
        'primary_not': primary_not,
     }

    return render(request, 'forman_hub/main.html', context=data)
