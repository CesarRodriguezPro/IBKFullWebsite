from django.shortcuts import render
from Forman_hub.FuntionRoot import itcontrol
from django.http import HttpResponse


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


def data_collection(request, location_request=None):

    first_name                       = request.user.first_name
    last_name                        = request.user.last_name
    active                           = itcontrol.ItControl(first_name, last_name, location_request)
    list_locations                   = active.get_list_of_location()
    current_working_locations        = active.current_working_locations()
    current_location_label           = active.current_location()[1]



    data = {
        'current_employees': active.current_employees_count(),
        'list_of_devices': active.list_of_devices(),
        'list_locations': list_locations,
        'current_working_locations':current_working_locations,
        'current_location_label': current_location_label,
    }
    return data


def main_view(request):
    data = data_collection(request, location_request='allLocations')
    if request.method == 'POST':
        form = request.POST
        if len(list(form.keys())) > 1 and list(form.keys())[1] == 'download_current':
                return download_current_list(request)
        else:      
            location_request = list(form.keys())[1] if len(list(form.keys())) > 1 else 'allLocations'
            data = data_collection(request, location_request = location_request)
            return render(request, 'office/main.html', context=data)
    return render(request, 'office/main.html', context=data)
