from django.shortcuts import render
from .forms import RequestVacationForm
from .models import vacationRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .pdf_creator import pdf_resource


@login_required()
def vacation_request(request):
    request_vacation_form = RequestVacationForm()
    if request.method == "POST":
        request_vacation_form = RequestVacationForm(request.POST)
        if request_vacation_form.is_valid():
            form = request_vacation_form.save(commit=False)
            form.foreman = f"{request.user.first_name} {request.user.last_name}"
            form.save()
            pdf_resource(request)
            return HttpResponseRedirect(reverse('vacationRequest:vacation_viewinfo'))
    return render(request, "vacationRequest/vacationRequest.html", context={'form':request_vacation_form })


@login_required
def vacation_viewinfo(request):
    dict_items = vacationRequest.objects.all().order_by('date_submitted').reverse()
    return render(request, 'vacationRequest/viewinfo.html', context={'vacation_request_list': dict_items})


