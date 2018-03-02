from django.shortcuts import render
from django.utils import timezone
from .models import equipmentType

# Список доступного оборудования
def equipment_list(request):
    equipment = equipmentType.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'equipment_list.html', {'equipment': equipment})

