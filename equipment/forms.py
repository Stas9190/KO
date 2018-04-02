from django import forms

from .models import Equipment, Unit, Untigroup, Equip

class equipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('name', 'model',)

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
            'executor': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'time':forms.NumberInput(attrs={'step': 1, 'class': 'form-control', 'required': True, 'min': 0}),
            'periodicity':forms.NumberInput(attrs={'step': 1, 'class': 'form-control', 'required': True, 'min': 0}),
            'id_unitgroup': forms.Select(attrs={'class': 'form-control selectpicker show-tick'}),
            #'time': forms.Input(attrs={'class': 'form-control', 'required': True}),
        }

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
            'equipment_id': forms.Select(attrs={'class': 'form-control selectpicker show-tick'}),
            'units': forms.CheckboxSelectMultiple(),
        }

class unitGroupForm(forms.ModelForm):

    class Meta:
        model = Untigroup
        fields = '__all__'
        labels = {
            'name': 'Наименование'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }