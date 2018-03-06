from django import forms

from .models import equipmentType, Unit

class equipmentForm(forms.ModelForm):

    class Meta:
        model = equipmentType
        fields = ('name', 'model', 'inv_number',)

class unitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ('name', 'description', 'time', 'periodicity',)