from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import template
from UniversalRootFolder import itcontrol
from UniversalRootFolder.irregular_entries import IrregularEntries
from UniversalRootFolder.hours_greater import HoursGreater
from django.http import HttpResponse
from UniversalRootFolder import pdf_creator_for_timesheet
from django.views.generic import View
from django.contrib.auth.models import Group
from .models import CurrentPageModel
from .forms import CurrentLocationForm
import datetime

register = template.Library()


def download_current_list(request, location_request):
    first_name = request.user.first_name
    last_name  = request.user.last_name
    active     = itcontrol.ItControl(first_name, last_name, location_request)
    user = request.user

    if location_request == 'All Locations':
        csv_file = active.save_current_all()
        response = HttpResponse(csv_file, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{first_name}.{last_name}.allLocations.csv"'
        return response

    else:
        csv_file, location_name = active.save_current_by_location()
        response = HttpResponse(csv_file, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{first_name}.{last_name}.{location_name}.csv"'
        return response


def special_functions_dispatch(location_request):
    ''' Downloading data from timestation can make Website Slow down.
    with this function i will download this data only when i requested ALL location View.
    this will reduce the server use.'''

    if location_request == 'AllLocations':
        irregular = IrregularEntries()
        greater = HoursGreater()
        return irregular.send_to_website(), greater.get_times()
    else:
        return None, None


def data_collection(request, location_request):

    first_name                       = request.user.first_name
    last_name                        = request.user.last_name
    active                           = itcontrol.ItControl(first_name, last_name, location_request)
    list_locations                   = active.get_list_of_location()
    current_not, primary_not         = active.check_function()
    current_location_label           = active.current_location()[1]
    current_working_locations        = active.current_working_locations()
    irregular_entries, greater_hours = special_functions_dispatch(location_request)

    data = {
        'first_name':first_name,
        'last_name':last_name,
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
        'current_time': datetime.datetime.now().strftime('%m/%d/%Y %I:%M %p'),
    }
    return data

 
class Pdf(View):

    def get(self, request):
        current_location_p = itcontrol.ItControl(request.user.first_name, request.user.last_name, location_request=None)
        current_location = current_location_p.foreman_location()
        return pdf_creator_for_timesheet.pdf_builder(location=current_location)


@login_required
def foreman_main(request, requested_location = None, options=None):
    if options:
        if options == 'DownloadCurrent':
            return download_current_list(request, requested_location)
        elif options == 'last_week_timesheet':
            return pdf_creator_for_timesheet.pdf_builder_last_week(location=requested_location)
        elif options == 'current_Timesheet':
            if datetime.date.today().weekday() == 0:
                return pdf_creator_for_timesheet.pdf_builder_last_week(location=requested_location)
            else:
                return pdf_creator_for_timesheet.pdf_builder_current(location=requested_location)

    data = data_collection(request, requested_location)
    return render(request, 'forman_hub/main.html', context=data)

