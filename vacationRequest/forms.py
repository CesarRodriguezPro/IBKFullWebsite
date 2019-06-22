from django import forms
from .models import vacationRequest

class RequestVacationForm(forms.ModelForm):
    
    class Meta:
        model = vacationRequest
        exclude = ['date_submitted', 'foreman', 'status']
        widgets = {
            'init_date': forms.DateInput(format=('%m-%d-%Y'),
                              attrs={'class':'form-control', 'type':'date'}),
            'final_date': forms.DateInput(format=('%m-%d-%Y'),
                              attrs={'class':'form-control', 'type':'date'}),
        } 