# equipment/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.equipment_list, name="home"),
    path('equipment/new/', views.equipmentCreateView, name='new_equipment'),
]