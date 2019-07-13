from django.shortcuts import render
from .forms import RequestVacationForm, SignatureForm
from .models import vacationRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .pdf_creator import pdf_resource
from jsignature.utils import draw_signature


@login_required()
def vacation_request(request):
    request_vacation_form = RequestVacationForm()
    forms = {
        'form': request_vacation_form,
    }
    if request.method == "POST":
        request_vacation_form = RequestVacationForm(request.POST)
        if request_vacation_form.is_valid():
            form = request_vacation_form.save(commit=False)
            form.foreman = f"{request.user.first_name} {request.user.last_name}"
            form.save()
            pdf_resource(request)
            return HttpResponseRedirect(reverse('vacationRequest:vacation_viewinfo'))
    return render(request, "vacationRequest/vacationRequest.html", context=forms)

@login_required
def vacation_viewinfo(request):
    dict_items = vacationRequest.objects.all().order_by('date_submitted').reverse()
    return render(request, 'vacationRequest/viewinfo.html', context={'vacation_request_list': dict_items})


