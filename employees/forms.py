from django.forms import ModelForm
from .models import Employees

class EmployeeForm(ModelForm):
    
    class Meta:
        model = Employees

