from django import forms
from .models import Bebida


class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ['nome', 'descricao', 'preco', 'quantidade', 'foto', 'isAlcoolico', 'estado']
        labels = {
            'nome': 'Nome da Bebida',
            'descricao': 'Breve Descrição',
            'preco': 'Preço',
            'quantidade': 'Quantidade',
            'foto': 'Foto',
            'isAlcoolico': 'É Alcoolico?',
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
            'quantidade': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'id': 'id_quantidade',
                    'name': 'quantidade',
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

class BebidaFormReadonly(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ['nome', 'descricao', 'preco', 'foto', 'quantidade', 'isAlcoolico', 'estado']
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
            'quantidade': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'step': '0.00001',
                    'id': 'id_quantidade',
                    'name': 'quantidade',
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