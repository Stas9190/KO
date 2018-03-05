from django import forms

from .models import equipmentType

class equipmentForm(forms.ModelForm):

    class Meta:
        model = equipmentType
        fields = ('name', 'model',)