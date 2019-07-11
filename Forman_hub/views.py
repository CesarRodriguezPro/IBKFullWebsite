from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import template
from UniversalRootFolder import itcontrol
from UniversalRootFolder.irregular_entries import IrregularEntries
from UniversalRootFolder.hours_greater import HoursGreater
from django.http import HttpResponse
from UniversalRootFolder import pdf_creator_for_timesheet
from django.views.generic import View

register = template.Library()


def download_current_list(request, location_request=None):
    first_name = request.user.first_name
    last_name  = request.user.last_name
    active     = itcontrol.ItControl(first_name, last_name,location_request=location_request)
    user = request.user

    if user.groups.filter(name='SystemAdmin').exists() or user.groups.filter(name='office').exists():
        csv_file = active.save_current_all()
        response = HttpResponse(csv_file, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{first_name}.{last_name}.allLocations.csv"'
        return response

    else:
        csv_file, location_name = active.save_current_by_location()
        response = HttpResponse(csv_file, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{first_name}.{last_name}.{location_name}.csv"'
        return response


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
        if len(list(form.keys())) > 1 and list(form.keys())[1] == 'download_current':
                return download_current_list(request)

        else:      
            location_request = list(form.keys())[1] if len(list(form.keys())) > 1 else 'allLocations'
            data = data_collection(request, location_request = location_request)
            return render(request, 'forman_hub/SystemAdmin.html', context=data)
    data = data_collection(request)
    return render(request, 'forman_hub/SystemAdmin.html', context=data)


class Pdf(View):

    def get(self, request):
        current_location_p = itcontrol.ItControl(request.user.first_name, request.user.last_name, location_request=None)
        current_location = current_location_p.foreman_location()
        return pdf_creator_for_timesheet.pdf_builder(location=current_location)


def timesheet_pass_pdf(request):
    current_location_p = itcontrol.ItControl(request.user.first_name, request.user.last_name, location_request=None)
    current_location = current_location_p.foreman_location()
    return pdf_creator_for_timesheet.pdf_builder(location=current_location)


@login_required
def foreman_main(request):
    user = request.user
    if user.groups.filter(name='Foreman').exists():
        if request.method == "POST":
            form = request.POST

            if list(form.keys())[1] == 'download_current':
                return download_current_list(request)
            elif len(list(form.keys())) > 1 and list(form.keys())[1] == 'past_time_sheet':
                return timesheet_pass_pdf(request)

        data = data_collection(request=request)
        return render(request, 'forman_hub/main.html', context=data)

    elif user.groups.filter(name='SystemAdmin').exists():
        return system_admin(request=request)

    else:
        return render(request, 'controlapp/home.html')
