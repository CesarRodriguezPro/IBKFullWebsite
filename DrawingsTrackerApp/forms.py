from django import forms
from .models import Drawings


class AddDrawings(forms.ModelForm):
    class Meta:
        model = Drawings
        fields = '__all__'

        widgets = {
            'date_submitted': forms.DateInput(format=('%m-%d-%Y'),
                              attrs={'class':'form-control', 'type':'date'}),
        }

class DeleteDrawings(forms.Form):
    detete_item = forms.CharField(label='IDCode to delete', max_length=100)
