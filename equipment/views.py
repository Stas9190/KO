from django.shortcuts import render
from django.utils import timezone
from .models import Equipment, Unit, Untigroup, Equip, EquipmentEquipUnits as eeu, Work, Executor, UnitCatalog, Location
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DeleteView, UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from ko_project import settings
from io import BytesIO
import os
from django.core.files.base import ContentFile

from reportlab.lib.pagesizes import letter, A4, inch, landscape
from reportlab.lib.styles import getSampleStyleSheet, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
styleSheet = getSampleStyleSheet()

# Импортируем формы
from .forms import equipmentForm, unitForm, equipForm, unitGroupForm, executorForm, unitCatalogForm

def equipment_list(request):
    equipment = Equipment.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'equipment_list.html', {'equipment': equipment})

def executor_list(request):
    executor = Executor.objects.all().order_by('executor')
    return render(request, 'executor_list.html', {'executor': executor})

#справочник узлов оборудования
def unit_catalog(request):
    unitCatalog = UnitCatalog.objects.all().order_by('pk')
    return render(request, 'unit_catalog.html', {'unitCatalog': unitCatalog})

def handle_uploaded_file(f):
     with open('equipment/media/media/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
'''
def equipmentCreateView(request):
    if request.method == "POST":
        form  = equipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            files = request.FILES.getlist('path')
            for f in files:
                handle_uploaded_file(f)
                loc = Location()
                loc.id_equipment = Equipment.objects.all().order_by('-id')[0]
                loc.path = 'equipment/media/media/'+f.name
                loc.save()
            return redirect("equipment_list")
    else:  
        form = equipmentForm
        return render(request, 'equipment_new.html', {'form': form})
'''

def executorCreateView(request):
    if request.method == "POST":
        form = executorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("executor_list")
    else:
        form = executorForm
        return render(request, 'executor_new.html', {'form': form})

def equipmentCreateView(request):
    if request.method == "POST":
        form = equipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("equipment_list")
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

def unitGroupCreateView(request):
    if request.method == "POST":
        form = unitGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("unitGroup")
    else:
        form = unitGroupForm
        return render(request, 'unitGroup_new.html', {'form': form})

def unitCatalogCreateView(request):
    if request.method == "POST":
        form = unitCatalogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("unit_catalog")
    else:
        form = unitCatalogForm
        return render(request, 'unitCatalog_new.html', {'form': form})


def unit_list(request):
    unit = Unit.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'unit_list.html', {'unit': unit}) 

def unitGroup(request):
    unitGroup = Untigroup.objects.all()
    return render(request, 'unitGroup.html', {'unitGroup': unitGroup})

# Обновление
class equipmentUpdateView(UpdateView):
    model = Equipment
    fields = ['group_name', 'model', 'photo']
    template_name = "edit.html"

class executorUpdateView(UpdateView):
    model = Executor
    fields = ['executor',]
    template_name = "edit.html"
    success_url = reverse_lazy('executor_list')

class unitUpdateView(UpdateView):
    model = Unit
    fields = ['name', 'id_unitgroup', 'description', 'executor', 'time', 'periodicity', 'notes', 'tools', 'photo']
    template_name = "edit.html"
    success_url = reverse_lazy('unit')

class unitGroupUpdateView(UpdateView):
    model = Untigroup
    fields = ['name']
    template_name = "edit.html"
    success_url = reverse_lazy('unitGroup')

class unitCatalogUpdateView(UpdateView):
    model = UnitCatalog
    fields = ['name']
    template_name = "edit.html"
    success_url = reverse_lazy('unit_catalog')

def junctionsUpdate(request, pk):
    if request.method == "POST":
        if 'changeOrder' in request.POST:
            data = request.POST.getlist('order')
            eeu_id = request.POST.getlist('eeu_id')
            for i in range(len(data)):
                #import pdb; pdb.set_trace()    НЕ УДАЛЯТЬ!!!!
                eeu.objects.filter(id=eeu_id[i]).update(order=data[i])
            return redirect("/junctions/"+str(pk)+"/edit/")
        else:
            instance = get_object_or_404(Equip, id = pk)
            form = equipForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            eeu_obj = eeu.objects.filter(equip_id = pk).order_by('order')
            i = 1
            for item in eeu_obj:
                eeu.objects.filter(pk=item.id).update(order=i)
                i += 1
            return redirect("home")
    else:
        # Все узлы, которые указаны в нашей карте
        selected_units = eeu.objects.raw('Select e.id, e.equip_id, e.[order], uc.name From equipment_equip_units e Inner Join Unit u on u.id = e.unit_id Inner Join Unit_catalog uc on uc.id = u.name where e.equip_id = %s order by e.[order]', [pk])

        inv_number = Equip.objects.filter(pk=pk)
        equipments = Equipment.objects.all()
        units = Unit.objects.raw('Select u.id, u.id_unitGroup, u.name, ug.name [group] From Unit u INNER Join untiGroup ug on ug.id = u.id_unitGroup Order By ug.id')
        groups = Untigroup.objects.all().order_by('id')
        selectedEquip = Equipment.objects.raw('Select id From Equipment Where id in (Select equipment_id_id From equipment_equip where id = %s)', [pk])
        tid = 0
        for item in selectedEquip:
            tid = item.id
        checkedUnit = Unit.objects.raw('Select id From Unit where id in (Select unit_id From equipment_equip_units where equip_id = %s)', [pk])
        uid = []
        for item in checkedUnit:
            uid.append(item.id)
        context = {'groups': groups, 'units': units, 'equipments': equipments, 'inv_number': inv_number, 'selectedEquip': tid, 'checkedUnits': uid, 'selected_units': selected_units}
        return render(request, 'equip_edit.html', context)

# Удаление
class equipmentDeleteView(DeleteView):
    model = Equipment
    template_name = "delete.html"
    success_url = reverse_lazy('equipment_list')

class unitDeleteView(DeleteView):
    model = Unit
    template_name = "delete.html"
    success_url = reverse_lazy('unit')

class junctionsDeleteView(DeleteView):
    model = Equip
    template_name = "delete.html"
    success_url = reverse_lazy('home')

class unitGroupDeleteView(DeleteView):
    model = Untigroup
    template_name = "delete.html"
    success_url = reverse_lazy("unitGroup")

class unitCatalogDeleteView(DeleteView):
    model = UnitCatalog
    template_name = "delete.html"
    success_url = reverse_lazy("unit_catalog")

class executorDeleteView(DeleteView):
    model = Executor
    template_name = "delete.html"
    success_url = reverse_lazy("executor_list")

# Создание привязки между узлами и оборудованием (EQUIP)!!!!!!
def junctions(request):
    equipList = Equip.objects.raw('SELECT ee.id, u.name name, e.model model, ee.ktp_name inv_number FROM equipment_equip ee INNER JOIN Equipment e ON e.id = ee.equipment_id_id INNER JOIN untiGroup u on e.group_name = u.id')
    return render(request, 'junctions.html', {'equipList': equipList})

def new_junctions(request):
    if request.method == "POST":
        form = equipForm(request.POST)
        if form.is_valid():
            units = request.POST.getlist('units')
            equip = Equip.objects.create(ktp_name=request.POST.get("ktp_name"), equipment_id_id=request.POST.get("equipment_id"))
            i = 1
            for item in units:
                eeu_model = eeu(equip=equip, unit=Unit.objects.get(pk=item), order=i)    
                eeu_model.save()
                i += 1
            return redirect("home")
    else:
        equipments = Equipment.objects.all()
        units = Unit.objects.raw('Select u.id, u.id_unitGroup, u.name, ug.name [group] From Unit u INNER Join untiGroup ug on ug.id = u.id_unitGroup Order By ug.id')
        groups = Untigroup.objects.all().order_by('id')
        form = equipForm
        context = {'form': form, 'groups': groups, 'units': units, 'equipments': equipments}
        return render(request, 'junctions_new.html', context)
    
# Карты обслуживания
def service(request):
    serviceList = Equip.objects.raw('SELECT ee.id, e.name, ee.ktp_name inv_number, e.model FROM equipment_equip ee INNER JOIN Equipment e ON e.id = ee.equipment_id_id')
    return render(request, 'serviceList.html', {'serviceList': serviceList})

def maintenance(request, pk):
    mList = Equip.objects.raw('Select ex.executor, eu.id, ug.name e_name, uc.name u_name, u.description, u.time, u.periodicity, u.photo, eu.fact, u.notes, u.tools FROM equipment_equip_units eu INNER JOIN equipment_equip ee ON ee.id = eu.equip_id INNER JOIN Equipment e ON e.id = ee.equipment_id_id INNER JOIN Unit u ON u.id = eu.unit_id LEFT JOIN Executor ex ON ex.id = u.executor INNER JOIN untiGroup ug ON ug.id = e.group_name INNER JOIN Unit_catalog uc ON uc.id = u.name WHERE ee.id = %s order by eu.[order]', [pk])
    context = {'pk': pk, 'mList': mList, 'MEDIA_URL': settings.MEDIA_URL}
    return render(request, 'maintenance.html', context)
    
# Выполнить обслуживание оборудования
def to_perform(request, pk):
    eeu.objects.filter(pk=pk).update(fact=0)

    current_user = request.user
    work = Work()
    work.id_user = current_user.id
    work.id_maintaince = pk
    work.date = timezone.now()
    work.save()

    mList = Equip.objects.raw('Select eu.id, e.name e_name, u.name u_name, u.description, u.time, u.periodicity, u.photo, eu.fact FROM equipment_equip_units eu INNER JOIN equipment_equip ee ON ee.id = eu.equip_id INNER JOIN Equipment e ON e.id = ee.equipment_id_id INNER JOIN Unit u ON u.id = eu.unit_id WHERE ee.id in (Select equip_id From equipment_equip_units Where id = %s)', [pk])
    context = {'pk': pk, 'mList': mList, 'MEDIA_URL': settings.MEDIA_URL}
    return render (request, 'maintenance.html', context)


class PdfPrint:

    def __init__(self, buffer, pageSize):
        self.buffer = buffer
        # default format is A4
        if pageSize == 'A4':
            self.pageSize = landscape(A4)
        elif pageSize == 'Letter':
            self.pageSize = landscape(letter)
        self.width, self.height = self.pageSize
    
    def report(self, weather_history, title, pk):
        # set some characteristics for pdf document
        doc = SimpleDocTemplate(
            self.buffer,
            rightMargin=72,
            leftMargin=72,
            topMargin=0,
            bottomMargin=72,
            pagesize=self.pageSize)
        #styles = getSampleStyleSheet()
        #!!!! Подключаем шрифты
        MyFontObject = TTFont('Arial', './equipment/static/Fonts/arial.ttf')
        pdfmetrics.registerFont(MyFontObject)
        P01 = Paragraph(''' <font face="Arial"><i>КАРТА ОБСЛУЖИВАНИЯ ОБОРУДОВАНИЯ № </i></font>''', styleSheet["BodyText"])
        P02 = Paragraph(''' <font face="Arial"><i>Разработал </i></font>''', styleSheet["BodyText"])
        P04 = Paragraph(''' <font face="Arial"><i>Проверил </i></font>''', styleSheet["BodyText"])
        P05 = Paragraph(''' <font face="Arial"><i>Согласовал </i></font>''', styleSheet["BodyText"])
        P06 = Paragraph(''' <font face="Arial"><i>Утвердил </i></font>''', styleSheet["BodyText"])
        P42 = Paragraph(''' <font face="Arial"><i>ЗИП "ЭНЕРГОМЕРА"</i></font>''', styleSheet["BodyText"])
        P50 = Paragraph(''' <font face="Arial"><i>Лист</i></font>''', styleSheet["BodyText"])
        P70 = Paragraph(''' <font face="Arial"><i>Листов</i></font>''', styleSheet["BodyText"])
        P52 = Paragraph(''' <font face="Arial"><i>Цех</i></font>''', styleSheet["BodyText"])
        P62 = Paragraph(''' <font face="Arial"><i>Участок</i></font>''', styleSheet["BodyText"])
        P82 = Paragraph(''' <font face="Arial"><i>Измен.</i></font>''', styleSheet["BodyText"])
        # create document
        elements = []
        data= [['','','','','',P50,'',P70,'',],
               [P01,'','','','','','','','',],
               [P02,'','','',P42,P52,P62,'',P82,],
               ['','','','','','','','','',],
               [P04,'','','','','','','','',],
               [P05,'','','','','','','','',],
               [P06,'','','','','','','','',],]
        #t = Table(data, 1*[0.4*inch], 1*[0.4*inch])        
        t = Table(data, style=[
            ('GRID', (0,0),(-1,-1), 0.25, colors.black),
            ('SPAN', (0,0),(4, 0)),
            ('SPAN', (0,1),(4, 1)),
            ('SPAN', (5,0),(6, 0)),
            ('SPAN', (7,0),(8, 0)),
            ('SPAN', (5,1),(6, 1)),
            ('SPAN', (7,1),(8, 1)),
            ('SPAN', (0,2),(0, 3)),
            ('SPAN', (4,2),(4, 5)),
            ('SPAN', (4,6),(8, 6)),
            ('SPAN', (6,2),(7, 2)),
            ('SPAN', (6,3),(7, 3)),
            ('SPAN', (5,4),(5, 5)),
            ('SPAN', (6,4),(7, 5)),
            ('SPAN', (8,4),(8, 5)),
            ('VALIGN', (0,0),(4, 0), 'BOTTOM'),
            ('VALIGN', (0,2),(0, 2), 'MIDDLE'),
            ('VALIGN', (4,2),(4, 2), 'MIDDLE'),
            ('LINEABOVE', (0,1),(4,1), 0.1, colors.white),  #не прозрачно!
        ])
        t._argW[0]=3.3*cm # Set column width
        t._argW[1]=3.3*cm
        t._argW[2]=2.9*cm
        t._argW[3]=2.9*cm
        t._argW[4]=4.1*cm
        t._argW[5]=3.3*cm
        t._argW[6]=3.3*cm
        t._argW[7]=3.3*cm
        t._argW[8]=3.3*cm
        t._argH[0]=0.7*cm # Set column height
        t._argH[1]=0.7*cm
        t._argH[2]=0.7*cm
        t._argH[3]=0.7*cm
        t._argH[4]=0.7*cm
        t._argH[5]=0.7*cm
        t._argH[6]=0.7*cm
        elements.append(t)

        # Фото на стартовой странице
        photos = Equipment.objects.raw('Select id, photo From [Equipment] Where id in (Select equipment_id_id From equipment_equip Where id = %s)', [pk])
        I0 = Image(photos[0].photo)
        I0.drawHeight = 12*cm*I0.drawWidth / I0.drawWidth
        I0.drawWidth = 14*cm
        headerData = [[I0,],]
        headerTable = Table(headerData, style=[
            ('GRID', (0,0),(-1,-1), 0.25, colors.white),
        ])
        elements.append(headerTable)

        # Запрос к бд
        mList = Equip.objects.raw('Select eu.id, e.name e_name, e.model, uc.name u_name, u.description, u.time, u.periodicity, u.photo, u.notes, u.tools, ex.executor, eu.fact FROM equipment_equip_units eu INNER JOIN equipment_equip ee ON ee.id = eu.equip_id INNER JOIN Equipment e ON e.id = ee.equipment_id_id INNER JOIN Unit u ON u.id = eu.unit_id INNER JOIN Unit_catalog uc on u.name = uc.id INNER JOIN Executor ex ON ex.id = u.executor WHERE ee.id = %s', [pk])
        i = 1
        for item in mList:
            P20 = Paragraph('<font face="Arial">'+item.u_name+'</font>', styleSheet["BodyText"])
            P31 = Paragraph('<font face="Arial">'+item.description+'</font>', styleSheet["BodyText"])
            P32 = Paragraph('<font face="Arial">'+item.tools+'</font>', styleSheet["BodyText"])
            P21 = Paragraph('<font face="Arial">'+item.executor+'</font>', styleSheet["BodyText"])
            if item.periodicity == 0 or item.periodicity == '':
                P41 = Paragraph('<font face="Arial">'+item.notes+'</font>', styleSheet["BodyText"])
            else:
                P41 = item.periodicity
            P51 = Paragraph('<font face="Arial">'+str(item.time)+' мин</font>', styleSheet["BodyText"])

            I = Image('equipment/media/'+item.photo)
            I.drawHeight = 9*cm*I.drawHeight / I.drawWidth
            I.drawWidth = 9*cm
            contentData = [[i,I,P20,'','','',],
                           ['','',P21,P31,P41,P51,],
                           ['', '','',P32,''],]
            contentTable = Table(contentData, style=[
                ('GRID', (0,0),(-1,-1), 0.25, colors.black),
                ('SPAN', (0,0),(0, 2)),
                ('SPAN', (1,0),(1, 2)),
                ('SPAN', (2,0),(5, 0)),
                ('SPAN', (2,1),(2, 2)),
                ('SPAN', (4,1),(4, 2)),
                ('SPAN', (5,1),(5, 2)),
                ('VALIGN', (0,0),(0, 0), 'TOP'),
                ('ALIGN', (2,0),(4, 0), 'CENTER'),
                ('ALIGN', (1,0),(-1, -1), 'CENTER'),
                ('VALIGN', (1,0),(-1, -1), 'MIDDLE'),
                ])
            contentTable._argW[0]=1*cm
            contentTable._argW[1]=9*cm
            contentTable._argW[2]=5.35*cm
            contentTable._argW[3]=4.675*cm
            contentTable._argW[4]=4.675*cm
            contentTable._argW[5]=4.675*cm
            elements.append(contentTable)
            i += 1
        
        # create other flowables
        doc.build(elements)
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf

#!!!!!!!!!!!!!!!!!!!!!!!!! Генерируем PDF файл
def to_pdf(request, pk):
    response = HttpResponse(content_type='application/pdf')
    today = timezone.now()
    filename = 'Карта' + today.strftime('%Y-%m-%d')
    response['Content-Disposition'] = 'attachement; filename={0}.pdf'.format(filename)
    buffer = BytesIO()
    report = PdfPrint(buffer, 'A4')
    pdf = report.report('', 'Карта обслуживания', pk)
    response.write(pdf)
    return response
