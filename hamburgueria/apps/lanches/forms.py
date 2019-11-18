from django import forms
from .models import Lanche
from .models import LancheIngredientes


class LancheForm(forms.ModelForm):
    class Meta:
        model = Lanche
        fields = ['nome', 'descricao', 'preco', 'foto', 'estado']
        labels = {
            'nome': 'Nome do Lanche',
            'descricao': 'Breve Descrição',
            'preco': 'Preço',
            'foto': 'Foto',
            'estado': 'Esta Ativo?',
        }
        widgets = {
            'nome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nome do Lanche',
                    'id': 'id_nome',
                    'maxlength': '100',
                    'name': 'nome'
                }
            ),
            'descricao': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Descrição do Lanche',
                    'id': 'id_descricao',
                    'name': 'descricao'
                }
            ),
            'preco': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'step': '0.01',
                    'id': 'id_preco',
                    'name': 'preco',
                }
            ),
        }

class LancheFormReadonly(forms.ModelForm):
    class Meta:
        model = Lanche
        fields = ['nome', 'descricao', 'preco', 'foto', 'estado']
        labels = {
            'nome': 'Nome do Lanche',
            'descricao': 'Breve Descrição',
            'preco': 'Preço',
            'foto': 'Foto',
            'estado': 'Esta Ativo?',
        }
        widgets = {
            'nome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nome do Lanche',
                    'id': 'id_nome',
                    'maxlength': '100',
                    'name': 'nome',
                    'readonly':'readonly',
                }
            ),
            'descricao': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Descrição do Lanche',
                    'id': 'id_descricao',
                    'name': 'descricao',
                    'readonly':'readonly',
                }
            ),
            'preco': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'step': '0.01',
                    'id': 'id_preco',
                    'name': 'preco',
                    'readonly':'readonly',
                }
            ),
        }

class LancheIngredientesForm(forms.ModelForm):

    class Meta:
        model = LancheIngredientes
        fields = '__all__'