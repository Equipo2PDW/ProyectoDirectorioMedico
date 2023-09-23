from django.urls import path
from django.urls import include

from .views import (detail_view,
                    update_view,
                    delete_view,
                    list_view,
                    create_medico,
                    buscar_especialidad,
                    buscar_comuna,
                    buscar_especialidad_comuna
                    )

urlpatterns = [
    path('', list_view),
    path('detail_view/<id>', detail_view, name='detail_view'),
    path('create', create_medico),
    path('<id>/update', update_view),
    path('<id>/delete', delete_view ),
    path('buscar_especialidad/<especialidad>', buscar_especialidad),
    path('buscar_comuna/<comuna>', buscar_comuna),
    path('buscar_especialidad_comuna/<especialidad>/<comuna>', buscar_especialidad_comuna),
]
