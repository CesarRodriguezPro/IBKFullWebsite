from django.shortcuts import render
from .forms import RequestVacationForm
from .models import vacationRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail

# Create your views here.
@login_required
def vacation_request(request):
    request_vacation_form = RequestVacationForm()
    if request.method == "POST":
        request_vacation_form = RequestVacationForm(request.POST)
        if request_vacation_form.is_valid():
            form = request_vacation_form.save(commit=False)
            form.foreman = f"{request.user.first_name} {request.user.last_name}"
            form.save()


            return HttpResponseRedirect(reverse("vacationRequest:vacation_viewinfo"))
    return render(request, "vacationRequest/vacationRequest.html", context={'form':request_vacation_form })

@login_required
def vacation_viewinfo(request):
    dict_items = vacationRequest.objects.all()
    return render(request, 'vacationRequest/viewinfo.html',context={'list_vacations':dict_items})
