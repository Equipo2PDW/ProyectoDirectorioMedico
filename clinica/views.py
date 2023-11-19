from django.shortcuts import (render, 
                              HttpResponseRedirect,
                              get_object_or_404,
                              redirect)
from .forms import MedicoForm, CitaForm
# Create your views here.
from .models import Medico, citaMedica, Comuna, Especialidad
from django.contrib import messages


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
    context['data'] = Medico.objects.get(id = id)
    obj = get_object_or_404(Medico, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/clinica/list_view")
    return render(request, "delete_view.html", context)

def create_medico(request):
    context = {}
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Médico añadido correctamente.')
        return HttpResponseRedirect("/clinica/list_view")
    else:
        # Capturando los mensajes de error del formulario
        error_messages = form.errors.as_data()
        for field, error in error_messages.items():
            for err in error:
                messages.error(request, f"{field}: {err}")
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


def citas_view(request):
    context = {}
    context['citas'] = citaMedica.objects.all()

    return render(request, "citas_view.html", context)

def detalle_cita_view(request, id):
    context = {}
    context['data'] = citaMedica.objects.get(id=id)
    print(context['data'])  # Agregar esta línea para depurar
    return render(request, "appointment_detail_view.html", context)
 

def delete_cita(request, id):
    context = {}
    obj = get_object_or_404(citaMedica, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/clinica/citas_view")
    
    context['cita'] = obj  # Utiliza la instancia obtenida con get_object_or_404
    return render(request, "delete_cita_view.html", context)
    

def create_cita(request):
    context = {}
    form = CitaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cita añadida correctamente.', extra_tags='success')
        return HttpResponseRedirect("/clinica/citas_view")
    else:
        # Capturar mensajes de error del formulario
        error_messages = form.errors.as_data()
        for field, error in error_messages.items():
            for err in error:
                messages.error(request, f"{field}: {err}", extra_tags='error')
    context['form'] = form
    return render(request, "create_cita.html", context)


#BUSCADOR

def comunas_view(request):
    context = {}
    context['datacomunas'] = Comuna.objects.all()
    return render(request, "citas_view.html", context)

def especialidades_view(request):
    context = {}
    context['dataespe'] = Especialidad.objects.all()

    return render(request, "citas_view.html", context)

def todo_view(request): #muestra 
    context = {}
    context['datacomunas'] = Comuna.objects.all()
    context['dataespe'] = Especialidad.objects.all()
    context['dataset'] = citaMedica.objects.all()
    return render(request, "citas_view.html", context)



def vista_principal_busqueda(request):
    comunas = Comuna.objects.all()
    especialidades = Especialidad.objects.all()
    resultados = Medico.objects.all()
    context = {
        'comunas': comunas,
        'especialidades': especialidades
    }

    if request.method == 'POST':
        comunas = Comuna.objects.all()
        especialidades = Especialidad.objects.all()

        especialidad = request.POST.get('especialidad')
        comuna = request.POST.get('comuna')
        nombre_medico = request.POST.get('nombre_medico')

        resultados = Medico.objects.all()

        if especialidad:
            resultados = resultados.filter(especialidades__tipo=especialidad)
        
        if comuna:
            resultados = resultados.filter(sucursales__comuna__nombre=comuna)
        
        if nombre_medico:
            resultados = resultados.filter(nombre__icontains=nombre_medico)
        
        print("Especialidad:", especialidad)
        print("Comuna:", comuna)
        print("Nombre del Médico:", nombre_medico)

        context = {
            'comunas': comunas,
            'especialidades': especialidades,
            'resultados': resultados,
        }
        return render(request, "list_view.html", context)
    context = {
        'comunas': comunas,
        'especialidades': especialidades,
        'resultados': resultados,
    }
    return render(request, "list_view.html", context)