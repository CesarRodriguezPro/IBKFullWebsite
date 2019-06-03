from django.shortcuts import render
from .forms import AddDrawings,DeleteDrawings
from .models import Drawings
from django.contrib.auth.decorators import login_required

@login_required
def drawings_main(request):
    return render(request, 'DrawingsTracker/home.html')

@login_required
def drawings_add(request):

    add_drawings_form = AddDrawings()
    if request.method == "POST":
        add_drawings_form = AddDrawings(request.POST)
        if add_drawings_form.is_valid():
            new_drawings = add_drawings_form.save(commit=True)
    return render(request, 'DrawingsTracker/add.html', context={'form': add_drawings_form})

@login_required
def drawings_viewinfo(request):
    dict_items = Drawings.objects.all()
    return render(request, 'DrawingsTracker/viewinfo.html',context={'Drawings':dict_items})

@login_required
def drawings_delete(request):
    delete_form = DeleteDrawings()
    if request.method == "POST":
        id_code = request.POST.get('detete_item')
        Drawings.objects.filter(code_Id=f'{id_code}').delete()
    return render(request, 'DrawingsTracker/delete.html', context={'form_delete':delete_form})
