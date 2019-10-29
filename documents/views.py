from django.views.generic import TemplateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .forms import DocumentForm
from django.shortcuts import redirect
from .models import Document


class ListDocument(LoginRequiredMixin, ListView):
    model = Document


def delete_document(request, pk):
    print(pk)
    if request.method == 'POST':
        document = Document.objects.get(pk=pk)
        document.delete()
    return redirect('documents:list_documents')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('documents:list_documents')
    else:
        form = DocumentForm()
    return render(request, 'documents/upload.html', {
        'form': form
    })




