from django.shortcuts import render
from .forms import RequestAbsentForm
from .models import absentRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .pdf_creator import pdf_resource


# Create your views here.
@login_required
def absent_request(request):
    request_absent_form = RequestAbsentForm()
    if request.method == "POST":
        request_absent_form = RequestAbsentForm(request.POST)
        if request_absent_form.is_valid():
            form = request_absent_form.save(commit=False)
            form.foreman = f"{request.user.first_name} {request.user.last_name}"
            form.save()
            pdf_resource(request)
            return HttpResponseRedirect(reverse("absentRequest:absent_viewinfo"))
    return render(request, "absentRequest/absentRequest.html", context={'form':request_absent_form })

@login_required
def absent_viewinfo(request):
    dict_items = absentRequest.objects.all().order_by('date_submitted').reverse()
    return render(request, 'absentRequest/viewinfo.html',context={'list':dict_items})
