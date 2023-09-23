from django.shortcuts import (render, 
                              HttpResponseRedirect,
                              get_object_or_404,
                              redirect)
from .forms import MedicoForm
# Create your views here.
from .models import Medico

def list_view(request):
    context = {}
    context['dataset'] = Medico.objects.all()

    return render(request, "list_view.html", context)

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

def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Medico, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/clinica")
    return render(request, "delete_view.html", context)

def create_medico(request):
    context = {}
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_view')
    context['form'] = form
    return render(request, "create_medico.html", context)

#funcion para buscar un medico en base a especialidad, mostrar resultados de medicos en el sistema que esten en esa especialidad
def buscar_especialidad(request, especialidad):
    context = {}
    context['dataset'] = Medico.objects.filter(especialidades__tipo= especialidad)

    return render(request,"list_view.html", context)

def buscar_comuna(request, comuna):
    context = {}
    context['dataset'] = Medico.objects.filter(sucursales__comuna__nombre= comuna)

    return render(request,"list_view.html", context)

def buscar_especialidad_comuna(request, especialidad, comuna):
    context = {}
    context['dataset'] = Medico.objects.filter(especialidades__tipo= especialidad, sucursales__comuna__nombre= comuna)

    return render(request,"list_view.html", context)