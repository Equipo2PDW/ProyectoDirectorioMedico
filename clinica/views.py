from django.shortcuts import render, redirect
from .forms import MedicoForm
# Create your views here.
from .models import Medico

def detail_view(request, id):
    context = {}
    context['data'] = Medico.objects.get(id = id)

    return render(request, "detail_view.html", context)

def update_view(request, id):

    context = {}
    obj = Medico.objects.get(id = id)
    form = MedicoForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('detail_view', id=id)
    context['form'] = form

    return render(request, "update_view.html", context)