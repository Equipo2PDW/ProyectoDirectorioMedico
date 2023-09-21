from django.urls import path
from django.urls import include

from .views import detail_view, update_view

urlpatterns = [
    path('<id>', detail_view, name='detail_view'),
    path('<id>/update', update_view),
]
