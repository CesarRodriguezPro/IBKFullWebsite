from django import forms

class CurrentLocationForm(forms.Form):

    current_location = forms.CharField(max_length=20)
