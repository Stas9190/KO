from django import forms

from .models import Equipment, Unit, Untigroup, Equip

class equipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('name', 'model',)

'''
class junctionForm(forms.ModelForm):

    class Meta:
        model = Junction
        fields = ('id_equipment', 'id_unit')
        labels = {
            'id_unit': 'Выбор модуля',
            'id_equipment': 'Выбор типа оборудования',
        }
        widgets = {
            'id_unit': forms.CheckboxSelectMultiple(),
        }
'''

class unitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ('name', 'id_unitgroup', 'description', 'executor', 'time', 'periodicity', 'photo')
        labels = {
            'name': 'Наименование',
            'id_unitgroup': 'Выбор группы',
            'description': 'Описание работ',
            'time': 'Время выполнения',
            'periodicity': 'Периодичность выполнения',
            'photo': 'Изображение',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            #'time': forms.Input(attrs={'class': 'form-control', 'required': True}),
        }
    #name = forms.CharField(label="Наименование", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',}),)
    #description = forms.CharField(label="Описание работ", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',}),)
    #time = forms.DecimalField(label="Время выполнения (мин.)", decimal_places=0,)
    #periodicity = forms.DecimalField(label="Периодичность выполнения (дн.)", decimal_places=0,)
    #photo = forms.FileField(label="Изображение")

# Equip
class equipForm(forms.ModelForm):

    class Meta:
        model = Equip
        fields = '__all__'
        labels = {
            'inv_number': 'Инвентарный номер',
            'equipment_id': 'Тип оборудования',
            'units': 'Модуль оборудования',
        }
        widgets = {
            'inv_number': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            #'equipment_id': forms.Select(attrs={'class': 'form-control selectpicker show-tick'}),
            'units': forms.CheckboxSelectMultiple(),
        }  

'''
#class equipmentForm(forms.ModelForm):

#   class Meta:
#        model = equipmentType
#        fields = ('name', 'model', 'inv_number', 'units',)

class equipmentForm(forms.Form):
    name = forms.CharField(label="Наименование", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',}),)
    model = forms.CharField(label="Модель", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',}),)
    inv_number = forms.CharField(label="Инвентарный номер", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',}),)
    #equipment = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple)
    units = forms.MultipleChoiceField(
        label="Узлы",
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox',}),
        choices=Unit.objects.all().values_list('id', 'name'),
    )

class unitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ('name', 'description', 'time', 'periodicity',)
        '''