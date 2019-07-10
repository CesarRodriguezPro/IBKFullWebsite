from django import forms
from .models import vacationRequest
import datetime

class RequestVacationForm(forms.ModelForm):

    

    class Meta:
        today = datetime.date.today()
        date_in_3_weeks = today + datetime.timedelta(days=21)

        model = vacationRequest
        
        exclude = ['date_submitted', 'foreman', 'status']
        widgets = {
            'init_date': forms.DateInput(format=('%m-%d-%Y'),
                              attrs={'class':'form-control', 'type':'date'}),
            'final_date': forms.DateInput(format=('%m-%d-%Y'),
                              attrs={'class':'form-control', 'type':'date'}),
        } 