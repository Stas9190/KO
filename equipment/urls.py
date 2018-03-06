# equipment/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.equipment_list, name="home"),
    path('unit', views.unit_list, name="unit"),
    path('equipment/new/', views.equipmentCreateView, name='new_equipment'),
    path('unit/new/', views.unitCreateView, name='new_unit'),
    path('unit/<int:pk>/delete/', views.unitDeleteView.as_view(), name='unit_delete'),
    path('equipment/<int:pk>/edit/', views.equipmentUpdateView.as_view(), name='equipment_edit'),
    path('equipment/<int:pk>/delete/', views.equipmentDeleteView.as_view(), name='equipment_delete'),
    path('unit/<int:pk>/edit/', views.unitUpdateView.as_view(), name='unit_edit'),
    path('unit/<int:pk>/delete/', views.unitDeleteView.as_view(), name='unit_delete'),
]