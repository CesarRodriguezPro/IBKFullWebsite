from django.shortcuts import render
from django.views.generic import View, ListView
from .root_code.get_jnfo import GettingTimeSheet
from .root_code.verify_user import Verify
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from . import models
import datetime


def get_user_info(request, last, name):
    data = GettingTimeSheet()
    full_name = f'{last}, {name}'
    combine_time, separate_time, updated_time, next_update = data.run(full_name)
    record_request = models.RecordView()
    record_request.first_name = name
    record_request.last_name = last
    record_request.save()

    data = {
        'timestamp_log':updated_time,
        'next_update':next_update,
        'name' : full_name,
        'combine_data': combine_time,
        'separate_time': separate_time,
    }    

    return render(request, 'employees/employees_hub.html', context=data)


class Home(View):
    ''' this part for employees that don't have a main account '''
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name='employees/home.html')

    def post(self, request):

        last_name = request.POST.get('LastName')
        last_name = last_name.strip()
        card_number = request.POST.get('CardNumber')
        card_number = card_number.strip()
        active = Verify()
        full_name = active.verify(last_name, card_number)
        if full_name:
            list_name = full_name.split(',')
            last_name = list_name[0].strip()
            first_name = list_name[1].strip()
            return get_user_info(request, last_name, first_name)

        return HttpResponseRedirect(reverse('employees:Home'))


class EmployeesHub(View):
    ''' this is for employees who are part of the system as foremans or systemAdm'''
    def get(self, request, *args, **kwargs):
        name = request.user.first_name
        last = request.user.last_name
        return get_user_info(request,last,name)


class Record(ListView, LoginRequiredMixin):
    template_name = 'employees/record_list.html'
    model = models.RecordView
    paginate_by = 100  # if pagination is desired
    ordering = ['-time']



