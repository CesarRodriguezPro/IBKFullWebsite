from django import forms
from .models import absentRequest

class RequestAbsentForm(forms.ModelForm):
    
    class Meta:
        model = absentRequest
        exclude = ['date_submitted', 'foreman', 'status']
        widgets = {
            'init_date': forms.DateInput(format=('%m-%d-%Y'),
                              attrs={'class':'form-control', 'type':'date'}),
            'final_date': forms.DateInput(format=('%m-%d-%Y'),
                              attrs={'class':'form-control', 'type':'date'}),
        } 