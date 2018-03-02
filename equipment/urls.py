# equipment/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.equipment_list, name="equipmant_list"),
]