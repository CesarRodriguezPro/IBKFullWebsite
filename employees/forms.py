from django import forms
from .models import RecordView

class RecortForm(forms.ModelForm):
    class Meta:
        model = RecordView
        fields = ['last_name', 'first_name']
    