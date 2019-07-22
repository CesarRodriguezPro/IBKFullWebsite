from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from  .  import timesheet


class Render_file:
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)


def addact_label(dict_in):
    return_list = []
    for item in dict_in.values():
        item['Total_Hours'] = item.pop('Total Hours')
        return_list.append(item)
    return return_list


def pdf_builder_last_week(location):
    raw_data = timesheet.PreviousWeekTimeSheet(location=location)
    data = raw_data.run()
    label = [dates.keys() for dates in data.values()][0]

    params = {
        'timesheet_for': location,
        'labels': label,
        'data': addact_label(data),
    }
    return Render_file.render('forman_hub/timesheet_template.html', params)


def pdf_builder_current(location):
    raw_data = timesheet.CurrentWeekTimeSheet(location=location)
    data = raw_data.run()
    label = [dates.keys() for dates in data.values()][0]
    params = {
        'timesheet_for': location,
        'labels': label,
        'data': addact_label(data),
    }
    return Render_file.render('forman_hub/timesheet_template.html', params)


