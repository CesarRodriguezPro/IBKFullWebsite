
from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
