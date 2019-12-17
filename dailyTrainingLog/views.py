from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from weasyprint import HTML
from django.http import HttpResponse
from dailyTrainingLog.DataProccesing import GetDataFromTimeStation
import datetime


def building_pages(location, today):
    timestationData = GetDataFromTimeStation(location)
    data, not_in = timestationData.run()
 
    context = {
        'today_date': today,
        'employees_names':data,
        'not_in':not_in,
        'location':location
    }
    
    html_string = render_to_string('dailyTrainingLog/template.html', context=context)
    html = HTML(string=html_string)
    rendered_pdf = html.render()
    return [rendered_pdf]

@login_required
def dailyTrainigLog_pdf(request, location):
    today = datetime.datetime.now().strftime('%m/%d/%Y')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (f'inline; filename={location}-dailyTrainingLog-{today}.pdf')
    documents = building_pages(location, today)
    all_pages = [page for document in documents for page in document.pages]
    documents[0].copy(all_pages).write_pdf(response)
    return response

