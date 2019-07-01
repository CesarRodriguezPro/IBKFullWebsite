from django.shortcuts import render
from .forms import RequestVacationForm
from .models import vacationRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.mail import send_mail
from .render import Render_file
from threading import Thread, activeCount
from django.views.generic import View


''' working with this funtion to view and send email with pdfs'''
def send_email(file):
    
    # working in sending email.
    pass 
    
    send_email()


class Pdf(View):
    def get(self, request):
        params = {
            'current_date':'5/05/2019',
            'employee':'Cesar Rodriguez',
            'date_in': '10/23/2019',
            'date_out': '11/25/2019',
            'superviser': 'Tyrone McLance',
        }
        file = Render_file.render_to_file('vacationRequest/pdf.html', params)

        return Render_file.render('vacationRequest/pdf.html', params)


@login_required
def vacation_request(request):
    request_vacation_form = RequestVacationForm()
    if request.method == "POST":
        request_vacation_form = RequestVacationForm(request.POST)
        if request_vacation_form.is_valid():
            form = request_vacation_form.save(commit=False)
            form.foreman = f"{request.user.first_name} {request.user.last_name}"
            form.save()
            print('-----------------------------------> ', type(form))

            # return HttpResponseRedirect(reverse("vacationRequest:vacation_viewinfo"))
    return render(request, "vacationRequest/vacationRequest.html", context={'form':request_vacation_form })

@login_required
def vacation_viewinfo(request):
    dict_items = vacationRequest.objects.all()
    return render(request, 'vacationRequest/viewinfo.html',context={'list_vacations':dict_items})


if __name__ == "__main__":
    pass