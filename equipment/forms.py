from django import forms

from .models import equipmentType, Unit

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