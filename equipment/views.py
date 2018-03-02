from django.shortcuts import render

# Список доступного оборудования
def equipment_list(request):
    return render(request, 'equipment_list.html', {})
