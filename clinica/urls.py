from django.urls import path
from django.urls import include

from .views import (detail_view,
                    update_view,
                    delete_view,
                    list_view
                    )

urlpatterns = [
    path('', list_view),
    path('<id>', detail_view, name='detail_view'),
    path('<id>/update', update_view),
    path('<id>/delete', delete_view ),
]
