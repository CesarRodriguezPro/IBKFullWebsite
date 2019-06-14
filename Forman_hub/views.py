from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import template
from .FuntionRoot import itcontrol
from .FuntionRoot.irregular_entries import IrregularEntries
from .FuntionRoot.hours_greater import HoursGreater


register = template.Library()


def especial_funtions_dispatch(location_request):

    ''' Downloading data from timestation can make Website Slow down.
    with this function i will download this data only when i requested ALL location View.
    this will reduce the server use.'''

    if location_request == 'allLocations':
        irregular = IrregularEntries()
        greater = HoursGreater()
        return irregular.send_to_website(), greater.get_times()
    else:
        return None, None


def data_collection(request, location_request=None):

    first_name                       = request.user.first_name
    last_name                        = request.user.last_name
    active                           = itcontrol.ItControl(first_name, last_name, location_request)
    list_locations                   = active.get_list_of_location()
    current_not, primary_not         = active.check_function()
    current_location_label           = active.current_location()[1]
    current_working_locations        = active.current_working_locations()
    irregular_entries, greater_hours = especial_funtions_dispatch(location_request)
                 

    data = {
        'current_employees': active.current_employees_count(),
        'list_of_devices': active.list_of_devices(),
        'warning_not_today_clock_in': active.warning_not_today_clock_in,
        'current_not': current_not,
        'primary_not': primary_not, 
        'list_locations': list_locations,
        'current_location_label': current_location_label,
        'irregular_entries': irregular_entries,
        'current_working_locations':current_working_locations,
        'greater_hours': greater_hours,
    }
    return data


def system_admin(request):

    if request.method == 'POST':
        form = request.POST
        location_request = list(form.keys())[1] if len(list(form.keys())) > 1 else 'allLocations'
        data = data_collection(request, location_request = location_request)
        return render(request, 'forman_hub/SystemAdmin.html', context=data)
    
    data = data_collection(request)
    return render(request, 'forman_hub/SystemAdmin.html', context=data)


@login_required
def foreman_main(request):
    user = request.user
    if user.groups.filter(name='Foreman').exists():
        data = data_collection(request=request)
        return render(request, 'forman_hub/main.html', context=data)
    elif user.groups.filter(name='SystemAdmin').exists(): 
        return system_admin(request=request)
    else:
        return render(request, 'controlapp/home.html')
    




