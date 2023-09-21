from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Especialidad)
admin.site.register(Comuna)
admin.site.register(Estudios)
admin.site.register(Medico)
admin.site.register(Sucursal)
admin.site.register(Paciente)
admin.site.register(citaMedica)



