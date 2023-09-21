from django.urls import path
from django.urls import include

from .views import detail_view

urlpatterns = [
    path('<id>', detail_view),
]
