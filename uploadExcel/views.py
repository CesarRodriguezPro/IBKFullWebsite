from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from . import forms
import pandas as pd

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_TO_MEDIA = os.path.join(ROOT_PATH,'media')
PATH_TO_ROOT_DATA = os.path.join(PATH_TO_MEDIA, 'data.xlsx')
PATH_TO_TEST_DATA = os.path.join(PATH_TO_MEDIA, 'test','data.xlsx')



def check_excel_file():
    if os.path.isfile(PATH_TO_TEST_DATA):
        try:
            raw = pd.read_excel(PATH_TO_TEST_DATA)
            try:
                raw[['Employee name', 'TITLE', 'OSHA-30No', 'OSHA-30exp']]
                return [True, 'The File was sucessfully Saved']
            except:
                return [False, 'Please check that the file has "Employee name", "TITLE", "OSHA-30No", "OSHA-30exp"']
        except:
            return [False, 'The file Extension must be .xlsx ']
    else:
        return [True, 'The File Was succesfully Saved']

def delete_excelFile(path):
    try:
        os.remove(path)
    except:
        pass


@login_required()
def upload(request):
    if request.method == 'POST':
        form = forms.DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            delete_excelFile(PATH_TO_TEST_DATA)
            form.save()
            list_values = check_excel_file()
            if list_values[0] == True:
                messages.success(request, list_values[1])
                delete_excelFile(PATH_TO_ROOT_DATA)
                os.rename(PATH_TO_TEST_DATA, PATH_TO_ROOT_DATA)
            else:
                messages.error(request, list_values[1])

    form = forms.DocumentForm()
    return render(request, 'uploadExcel/index.html', context={'form':form})


if __name__ == "__main__":
    delete_excelFile()