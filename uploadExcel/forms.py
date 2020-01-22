from django import forms
from .models import ExcelUploadModel



class DocumentForm(forms.ModelForm):
    class Meta:
        model = ExcelUploadModel
        fields = ('file_name', 'document', )






