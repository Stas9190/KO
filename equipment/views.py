from django.shortcuts import render
from django.utils import timezone
from .models import equipmentType, Unit
from django.shortcuts import redirect
from django.views.generic import DeleteView, UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Импортируем формы
from .forms import equipmentForm, unitForm

# Список доступного оборудования
def equipment_list(request):
    equipment = equipmentType.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'equipment_list.html', {'equipment': equipment})

# Список узлов оборудования
def unit_list(request):
    unit = Unit.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'unit_list.html', {'unit': unit})

def equipmentCreateView(request):
    if request.method == "POST":
        form  = equipmentForm(request.POST)
        if form.is_valid():
            eq = equipmentType()
            eq.name = request.POST.get("name")
            eq.model = request.POST.get("model")
            eq.inv_number = request.POST.get("inv_number")
            eq.date = timezone.now()
            eq.save()
            return redirect("home")
    else:  
        form = equipmentForm
        return render(request, 'equipment_new.html', {'form': form})

def unitCreateView(request):
    if request.method == "POST":
        form  = unitForm(request.POST)
        if form.is_valid():
            un = Unit()
            un.name = request.POST.get("name")
            un.description = request.POST.get("description")
            un.time = request.POST.get("time")
            un.periodicity = request.POST.get("periodicity")
            un.date = timezone.now()
            un.save()
            return redirect("unit")
    else:  
        form = unitForm
        return render(request, 'unit_new.html', {'form': form})

# Удаление
class equipmentDeleteView(DeleteView):
    model = equipmentType
    template_name = "delete.html"
    success_url = reverse_lazy('home')

class unitDeleteView(DeleteView):
    model = Unit
    template_name = "delete.html"
    success_url = reverse_lazy('unit')

# Обновление
class equipmentUpdateView(UpdateView):
    model = equipmentType
    fields = ['name', 'model', 'inv_number']
    template_name = "edit.html"

class unitUpdateView(UpdateView):
    model = Unit
    fields = ['name', 'description', 'time', 'periodicity']
    template_name = "edit.html"
    success_url = reverse_lazy('unit')