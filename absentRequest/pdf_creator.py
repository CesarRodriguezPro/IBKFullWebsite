from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import os
from datetime import datetime
from django.core.mail import EmailMessage


sender = 'cesarr@ibkconstructiongroup.com'
to = ['cesarr@ibkconstructiongroup.com']


class Render_file:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)
    
    @staticmethod
    def render_to_file(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        file_name = "absentRequest.pdf"
        file_path = os.path.join(os.path.abspath(os.path.dirname("__file__")), "store", file_name)
        with open(file_path, 'wb') as pdf:
            pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
        return [file_name, file_path]


def send_mail_to_accounting(file, employee, foreman_email ):
    to_total = to.append(foreman_email)
    subject = f'Absent Request for {employee}'
    message = '''
    Lyuba,
    best,
    '''
    message = EmailMessage(subject, message, sender, to_total)
    message.attach_file(file[1])
    message.send()


def pdf_resource(request):
    '''get the information and group for the creating a pdf'''
    today_date = datetime.today().strftime('%m/%d/%Y')
    employee = request.POST.get('employee').title()
    foreman_email = request.user.email
    params = {
        'current_date':today_date,
        'employee':employee,
        'date_in': datetime.strftime(datetime.strptime(request.POST.get('init_date'),'%Y-%m-%d'), "%m/%d/%Y"),
        'date_out': datetime.strftime(datetime.strptime(request.POST.get('final_date'),'%Y-%m-%d'), "%m/%d/%Y"),
        'superviser': f"{request.user.first_name} {request.user.last_name} ".title(),
        'reason'    : request.POST.get('reason')
    }
   
    file=Render_file.render_to_file('absentRequest/pdf.html', params)
    # return Render_file.render('absentRequest/pdf.html', params)
    send_mail_to_accounting(file, employee, foreman_email)

