from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from  .  import previous_week_timesheet


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


def pdf_builder(location):

    raw_data = previous_week_timesheet.PreviousWeekTimeSheet(location=location)
    data = raw_data.run()
    group_dates = [dates.keys() for dates in data.values()][0]
    date = list(group_dates)[2:-1]
    params = {
        'timesheet_for': location,
        'group_dates': group_dates,
        'data': data,
    }
    return Render_file.render('forman_hub/timesheet_template.html', params)


