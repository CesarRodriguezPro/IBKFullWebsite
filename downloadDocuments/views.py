from django.views.generic import (TemplateView, CreateView, UpdateView,
                                   DeleteView, ListView, DeleteView, View)
from django.shortcuts import render


class list_view(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, "downloadDocuments/list_view.html")