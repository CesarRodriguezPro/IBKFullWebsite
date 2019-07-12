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


def pdf_builder_last_week(location):
    raw_data = timesheet.PreviousWeekTimeSheet(location=location)
    data = raw_data.run()
    group_dates = [dates.keys() for dates in data.values()][0]
    params = {
        'timesheet_for': location,
        'group_dates': group_dates,
        'data': data,
    }
    return Render_file.render('forman_hub/timesheet_template.html', params)


def pdf_builder_current(location):
    raw_data = timesheet.CurrentWeekTimeSheet(location=location)
    data = raw_data.run()
    group_dates = [dates.keys() for dates in data.values()][0]
    params = {
        'timesheet_for': location,
        'group_dates': group_dates,
        'data': data,
    }
    return Render_file.render('forman_hub/timesheet_template.html', params)


