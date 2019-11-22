from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from django.shortcuts import redirect
from .models import Document


class ListDocument(LoginRequiredMixin, ListView):
    model = Document

@login_required()
def delete_document(request, pk):
    print(pk)
    if request.method == 'POST':
        document = Document.objects.get(pk=pk)
        document.delete()
    return redirect('documents:list_documents')


@login_required()
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




