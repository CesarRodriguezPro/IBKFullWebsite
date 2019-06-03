from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import itcontrol


# Create your views here.
@login_required
def foreman_main(request):

    active = itcontrol.ItControl(location='262')
    current_not_primary, primary_no_current = active.check_function()
    print(current_not_primary)
    print(primary_no_current)

    data = {
        'current_employees': active.current_employees_count(),
        'list_of_devices': active.list_of_devices(),
        'warning_not_today_clock_in': active.warning_not_today_clock_in,
        'current_not_primary': current_not_primary,
        'primary_no_current': primary_no_current,
     }

    return render(request, 'forman_hub/main.html', context=data)
