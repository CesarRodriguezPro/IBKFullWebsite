from django import forms
from .models import UserMain

class RegistrationUser(forms.ModelForm):
    class Meta:
        model = UserMain
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            }
