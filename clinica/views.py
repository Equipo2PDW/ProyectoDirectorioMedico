from django.shortcuts import render

# Create your views here.
from .models import Medico

def detail_view(request, id):
    context = {}
    context['data'] = Medico.objects.get(id = id)

    return render(request, "Detail_view.html", context)