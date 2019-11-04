from django import forms
from .models import Lanche


class LancheForm(forms.ModelForm):
    class Meta:
        model = Lanche
        fields = ['nome', 'descricao', 'preco', 'foto', 'lancheIngrediente', 'estado']
        labels = {
            'nome': 'Nome do Lanche',
            'descricao': 'Breve Descrição',
            'preco': 'Preço',
            'foto': 'Foto',
            'lancheIngrediente': 'Ingredientes',
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
            'lancheIngrediente': forms.SelectMultiple(
                attrs = {
                    'class': 'form-control',
                }
            ),
        }

class LancheFormReadonly(forms.ModelForm):
    class Meta:
        model = Lanche
        fields = ['nome', 'descricao', 'preco', 'foto', 'lancheIngrediente', 'estado']
        labels = {
            'nome': 'Nome do Lanche',
            'descricao': 'Breve Descrição',
            'preco': 'Preço',
            'foto': 'Foto',
            'lancheIngrediente': 'Ingredientes',
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
            'lancheIngrediente': forms.SelectMultiple(
                attrs = {
                    'class': 'form-control',
                    'disabled':'disabled',
                }
            ),
        }