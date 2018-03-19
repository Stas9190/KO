from django.shortcuts import render
from django.utils import timezone
from .models import Equipment, Unit, Untigroup, Equip
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView, UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from ko_project import settings

# Импортируем формы
from .forms import equipmentForm, unitForm, equipForm

def equipment_list(request):
    equipment = Equipment.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'equipment_list.html', {'equipment': equipment})

def equipmentCreateView(request):
    if request.method == "POST":
        form  = equipmentForm(request.POST)
        if form.is_valid():
            eq = Equipment()
            eq.name = request.POST.get("name")
            eq.model = request.POST.get("model")
            #eq.inv_number = request.POST.get("inv_number")
            eq.date = timezone.now()
            eq.save()
            return redirect("home")
    else:  
        form = equipmentForm
        return render(request, 'equipment_new.html', {'form': form})

def unitCreateView(request):
    if request.method == "POST":
        form  = unitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("unit")        
    else:  
        form = unitForm
        return render(request, 'unit_new.html', {'form': form})

def unit_list(request):
    unit = Unit.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'unit_list.html', {'unit': unit}) 

# Обновление
class equipmentUpdateView(UpdateView):
    model = Equipment
    fields = ['name', 'model',]
    template_name = "edit.html"

class unitUpdateView(UpdateView):
    model = Unit
    fields = ['name', 'id_unitgroup', 'description', 'executor', 'time', 'periodicity', 'photo']
    template_name = "edit.html"
    success_url = reverse_lazy('unit')

# Удаление
class equipmentDeleteView(DeleteView):
    model = Equipment
    template_name = "delete.html"
    success_url = reverse_lazy('home')

class unitDeleteView(DeleteView):
    model = Unit
    template_name = "delete.html"
    success_url = reverse_lazy('unit')

class junctionsDeleteView(DeleteView):
    model = Equip
    template_name = "delete.html"
    success_url = reverse_lazy('junctions')

# Создание привязки между узлами и оборудованием (EQUIP)!!!!!!
def junctions(request):
    equipList = Equip.objects.raw('SELECT e.id, e.name name, e.model model, ee.inv_number inv_number FROM equipment_equip ee INNER JOIN Equipment e ON e.id = ee.equipment_id_id')
    return render(request, 'junctions.html', {'equipList': equipList})

def new_junctions(request):
    if request.method == "POST":
        form = equipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/junctions")
    else:
        form = equipForm
        return render(request, 'junctions_new.html', {'form': form})
    
# Карты обслуживания
def service(request):
    serviceList = Equip.objects.raw('SELECT ee.id, e.name, ee.inv_number, e.model FROM equipment_equip ee INNER JOIN Equipment e ON e.id = ee.equipment_id_id')
    return render(request, 'serviceList.html', {'serviceList': serviceList})

def maintenance(request, pk):
    mList = Equip.objects.raw('Select eu.id, e.name e_name, u.name u_name, u.description, u.time, u.periodicity, u.photo FROM equipment_equip_units eu INNER JOIN equipment_equip ee ON ee.id = eu.equip_id INNER JOIN Equipment e ON e.id = ee.equipment_id_id INNER JOIN Unit u ON u.id = eu.unit_id WHERE ee.id = %s', [pk])
    context = {'pk': pk, 'mList': mList, 'MEDIA_URL': settings.MEDIA_URL}
    return render(request, 'maintenance.html', context)
    
    
    
'''    
    if request.method == "POST":
        #form  = junctionForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect("/junctions")        
    #else:  
        #form = junctionForm
        #return render(request, 'junctions_new.html', {'form': form})
        equipment = request.POST.get("equipment_type")
        #units = request.POST.getlist("array")
        units = {7, 8,}
        for item in units:
            j = Junction()
            j.id_unit = item
            j.id_equipment = equipment
            #save_to_database(units, equipment)
            j.save()
        return redirect("/junctions")
    else:  
        #form = junctionForm
        equipments = Equipment.objects.filter(date__lte=timezone.now()).order_by('date')
        units = Unit.objects.all()
        context = {'equipments': equipments, 'units': units}
        return render(request, 'junctions_new.html', context)
'''
'''
# Список доступного оборудования
def equipment_list(request):
    equipment = equipmentType.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'equipment_list.html', {'equipment': equipment})

# Список узлов оборудования
def unit_list(request):
    unit = Unit.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'unit_list.html', {'unit': unit})

def save_data(request):
    e = equipmentType.objects.get(id=13)
    u = Unit.objects.get(id=request.POST.get("units"))
    e.units.add(u)

def equipmentCreateView(request):
    if request.method == "POST":
        form  = equipmentForm(request.POST)
        if form.is_valid():
            eq = equipmentType()
            eq.name = request.POST.get("name")
            eq.model = request.POST.get("model")
            eq.inv_number = request.POST.get("inv_number")
            #eq.units = request.POST.get("units")
            #e = equipmentType.objects.get(id=request.POST.get("pk"))
            #u = Unit.objects.get(id=request.POST.get("units"))
            #e.entry_set.add(u)
            eq.date = timezone.now()
            eq.save()
            save_data(request)
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
'''