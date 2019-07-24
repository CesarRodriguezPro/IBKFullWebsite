from django.shortcuts import render
from .models import Employees
from django.views.generic import (TemplateView, CreateView, ListView, 
                                UpdateView, DeleteView ,DetailView)


class EmployeeMainView(TemplateView):
    template_name = 'employees/main.html'


class EmployeeCreateView(CreateView):
    model = Employees
    fields = ['employee']


class EmployeeUpdateView(UpdateView):
    model = Employees
    fields = ['employee']


class EmployeeDeleteView(DeleteView):
    model = Employees


class EmployeeListView(ListView):
    model = Employees


class EmployeeDetailView(DetailView):
    model = Employees

