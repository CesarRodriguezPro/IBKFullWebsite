from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'documents/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'documents/upload.html')


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'documents/home.html'



