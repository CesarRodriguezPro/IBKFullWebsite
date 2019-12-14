from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .rootApplications import timeStationServerInfo
import datetime
import os


class Home(TemplateView):
    template_name = 'dailySafety/index.html'


class PDF(TemplateView):
    template_name = os.path.join('dailySafety/template.html')


def building_pages(location):
    get_data = timeStationServerInfo.TimeStationInfo()
    list_devices = get_data.list_devices(location)
    date = datetime.datetime.now().strftime('%m/%d/%Y')

    list_pages = []
    counter = 1
    for device in list_devices:
        employees, number_employees = get_data.run(location, device)

        extra_space_right = 36 - number_employees if number_employees < 36 else 0
        extra_space_right_column = ['_' for x in range(extra_space_right)]
        extra_space_left_column = ['_' for x in range(8)]

        data = {
            'location': location,
            'date_time': f"7:00 am {date}",
            'number_employees': number_employees,
            'foreman_name': device,
            'items': employees,
            'extra_space_right_string' : extra_space_right_column,
            'extra_space_left_string' : extra_space_left_column,
            'list_topics' : timeStationServerInfo.list_topics,
        }
        html_string = render_to_string('dailySafety/template.html', context=data)
        html = HTML(string=html_string)
        rendered_pdf = html.render()
        list_pages.append(rendered_pdf)
        counter += 1
    return list_pages

def print_pdf(request, location):
    today = datetime.datetime.now().strftime('%m.%d.%Y')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (f'inline; filename={location}-DailySafety-{today}.pdf')
    documents = building_pages(location)

    all_pages = [page for document in documents for page in document.pages]
    documents[0].copy(all_pages).write_pdf(response)
    return response

    

