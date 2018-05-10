# equipment/urls.py
from django.urls import path
from django.conf.urls.static import static
from ko_project import settings
from . import views

urlpatterns = [
    path('', views.junctions, name="home"),
    path('unit', views.unit_list, name="unit"),
    path('unit/new/', views.unitCreateView, name='new_unit'),
    path('unit/<int:pk>/edit/', views.unitUpdateView.as_view(), name='unit_edit'),
    path('unit/<int:pk>/delete/', views.unitDeleteView.as_view(), name='unit_delete'),
    path('equipment_list', views.equipment_list, name='equipment_list'),
    path('equipment/new/', views.equipmentCreateView, name='new_equipment'),
    path('equipment/<int:pk>/edit/', views.equipmentUpdateView.as_view(), name='equipment_edit'),
    path('equipment/<int:pk>/delete/', views.equipmentDeleteView.as_view(), name='equipment_delete'),
    path('executor_list', views.executor_list, name='executor_list'),
    path('executor/<int:pk>/edit/', views.executorUpdateView.as_view(), name='executor_edit'),
    path('executor/new/', views.executorCreateView, name='new_executor'),
    path('executor/<int:pk>/delete/', views.executorDeleteView.as_view(), name='executor_delete'),
    path('unitGroup/new/', views.unitGroupCreateView, name='unitGroup_new'),
    path('unitGroup/<int:pk>/delete/', views.unitGroupDeleteView.as_view(), name='unitGroup_delete'),
    path('unitGroup/<int:pk>/edit/', views.unitGroupUpdateView.as_view(), name='unitGroup_edit'),
    path('unitGroup', views.unitGroup, name='unitGroup'),
    path('junctions/<int:pk>/delete/', views.junctionsDeleteView.as_view(), name='junctions_delete'),
    path('junctions/<int:pk>/edit/', views.junctionsUpdate, name='junctions_edit'),
    path('junctions/new_junctions', views.new_junctions, name='new_junctions'),
    path('service', views.service, name='service'),
    path('service/<int:pk>/maintenance/', views.maintenance, name='maintenance'),
    path('service/<int:pk>/to_perform/', views.to_perform, name='to_perform'),
    path('<int:pk>/to_pdf', views.to_pdf, name='to_pdf'),
    path('unit_catalog', views.unit_catalog, name='unit_catalog'),
    path('unitCatalog/new/', views.unitCatalogCreateView, name='unitCatalog_new'),
    path('unitCatalog/<int:pk>/edit/', views.unitCatalogUpdateView.as_view(), name='unitCatalog_edit'),
    path('unitCatalog/<int:pk>/delete/', views.unitCatalogDeleteView.as_view(), name='unitCatalog_delete'),
    path('route_card', views.route_card_list, name='route_card'),
    path('route_card/new/', views.new_route_card, name='new_route_card'),
    path('route_card/<int:pk>/delete/', views.routeCardDeleteView.as_view(), name='route_card_delete'),
    path('route_card/<int:pk>/edit/', views.routeCardsUpdate, name='route_card_edit'),
    path('route_card/<int:pk>/ktp_in_route_card/', views.ktp_in_route_card, name='ktp_in_route_card'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)