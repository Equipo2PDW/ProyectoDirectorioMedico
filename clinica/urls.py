from django.urls import path
from django.urls import include

from .views import (detail_view,
                    update_view,
                    delete_view,
                    list_view,
                    create_medico,
                    buscar_especialidad,
                    buscar_comuna,
                    buscar_especialidad_comuna,
                    create_cita,
                    citas_view,
                    comunas_view,
                    todo_view,
                    especialidades_view,
                    vista_principal_busqueda,
                    delete_cita
                    )

urlpatterns = [
    path('list_view', vista_principal_busqueda),
    path('detail_view/<id>', detail_view, name='detail_view'),
    path('create', create_medico, name='create_medico'),
    path('<id>/update', update_view),
    path('<id>/delete', delete_view ),
    path('buscar_especialidad/<especialidad>', buscar_especialidad),
    path('buscar_comuna/<comuna>', buscar_comuna),
    path('buscar_especialidad_comuna/<especialidad>/<comuna>', buscar_especialidad_comuna),
    path('citas_view', todo_view),
    path('clinica/delete_cita/<id>/', delete_cita, name='delete_cita'),
    path('create_cita', create_cita),
]
