from django.shortcuts import render
from django.utils import timezone
from .models import equipmentType
from django.shortcuts import redirect

# Импортируем формы
from .forms import equipmentForm

# Список доступного оборудования
def equipment_list(request):
    equipment = equipmentType.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'equipment_list.html', {'equipment': equipment})

def equipmentCreateView(request):
    if request.method == "POST":
        form  = equipmentForm(request.POST)
        if form.is_valid():
            eq = equipmentType()
            eq.name = request.POST.get("name")
            eq.model = request.POST.get("model")
            eq.date = timezone.now()
            eq.save()
            return redirect("home")
    else:  
        form = equipmentForm
        return render(request, 'equipment_new.html', {'form': form})