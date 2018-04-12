from django import forms

from .models import Equipment, Unit, Untigroup, Equip, Executor, UnitCatalog

class executorForm(forms.ModelForm):

    class Meta:
        model = Executor
        fields = ('executor',)
        widgets = {
            'executor': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }

class equipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('group_name', 'model', 'photo',)
        labels = {
            'group_name' : 'Наименование',
            'model' : 'Модель',
            'photo' : 'Изображение'
        }
        widgets = {
            'group_name': forms.Select(attrs={'class': 'form-control selectpicker show-tick'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }

class unitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ('name', 'id_unitgroup', 'description', 'executor', 'time', 'periodicity', 'notes', 'tools', 'photo')
        labels = {
            'name': 'Наименование',
            'id_unitgroup': 'Выбор группы',
            'description': 'Описание работ',
            'time': 'Время выполнения (мин)',
            'periodicity': 'Периодичность выполнения (дн)',
            'notes': 'Примечания',
            'tools': 'Инструмент, материалы',
            'photo': 'Изображение',
        }
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control selectpicker show-tick'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'executor': forms.Select(attrs={'class': 'form-control selectpicker show-tick'}),
            'time':forms.NumberInput(attrs={'step': 1, 'class': 'form-control', 'required': True, 'min': 0}),
            'periodicity':forms.NumberInput(attrs={'step': 1, 'class': 'form-control', 'required': True, 'min': 0}),
            'notes':forms.TextInput(attrs={'class': 'form-control',}),
            'tools':forms.TextInput(attrs={'class': 'form-control',}),
            'id_unitgroup': forms.Select(attrs={'class': 'form-control selectpicker show-tick'}),            
        }

class equipForm(forms.ModelForm):

    class Meta:
        model = Equip
        fields = '__all__'
        labels = {
            'ktp_name': 'Наименование ктп',
            'equipment_id': 'Тип оборудования',
            'units': 'Модуль оборудования',
        }
        widgets = {
            'ktp_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
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

class unitCatalogForm(forms.ModelForm):

    class Meta:
        model = UnitCatalog
        fields = '__all__'
        labels = {
            'name': 'Наименование'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }