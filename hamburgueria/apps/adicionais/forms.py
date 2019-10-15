from django import forms
from .models import Adicional
class AdicionalForm(forms.ModelForm):
    class Meta:
        model = Adicional