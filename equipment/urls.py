# equipment/urls.py
from django.urls import path
from django.conf.urls.static import static
from ko_project import settings
from . import views

urlpatterns = [
    path('', views.equipment_list, name="home"),
    path('unit', views.unit_list, name="unit"),
    path('junctions', views.junctions, name='junctions'),
    path('equipment/new/', views.equipmentCreateView, name='new_equipment'),
    path('unit/new/', views.unitCreateView, name='new_unit'),
    path('equipment/<int:pk>/edit/', views.equipmentUpdateView.as_view(), name='equipment_edit'),
    path('equipment/<int:pk>/delete/', views.equipmentDeleteView.as_view(), name='equipment_delete'),
    path('unit/<int:pk>/edit/', views.unitUpdateView.as_view(), name='unit_edit'),
    path('unit/<int:pk>/delete/', views.unitDeleteView.as_view(), name='unit_delete'),
    path('junctions/<int:pk>/delete/', views.junctionsDeleteView.as_view(), name='junctions_delete'),
    path('junctions/new_junctions', views.new_junctions, name='new_junctions'),
    path('service', views.service, name='service'),
    path('service/<int:pk>/maintenance/', views.maintenance, name='maintenance'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)