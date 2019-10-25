from django import forms
from .models import Adicional


class AdicionalForm(forms.ModelForm):
    class Meta:
        model = Adicional
        fields = ['nome', 'preco', 'quantidade', 'unidade', 'estado', 'descricao', 'adicionalFornecedor']
        labels = {
            'nome': 'Nome do Adicional',
            'preco': 'Preço do Adicional',
            'quantidade': 'Quantidade',
            'unidade': 'Unidade',
            'estado': 'Esta Ativo?',
            'descricao': 'Breve Descrição',
            'adicionalFornecedor': 'Fornecedores do Adicional',
        }
        widgets = {
            'nome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nome do Adicional',
                    'id': 'id_nome',
                    'maxlength': '100',
                    'name': 'nome'
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
            'quantidade': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'step': '0.00001',
                    'id': 'id_quantidade',
                    'name': 'quantidade',
                }
            ),
            'unidade': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Unidade de Medida',
                    'id': 'id_unidade',
                    'maxlength': '3',
                    'name': 'unidade'
                }
            ),
            'descricao': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Descrição do Adicional',
                    'id': 'id_descricao',
                    'name': 'descricao'
                }
            ),
            'adicionalFornecedor': forms.SelectMultiple(
                attrs = {
                    'class': 'form-control',
                }
            )
        }

class AdicionalFormReadonly(forms.ModelForm):
    class Meta:
        model = Adicional
        fields = ['nome', 'preco', 'quantidade', 'unidade', 'estado', 'descricao', 'adicionalFornecedor']
        labels = {
            'nome': 'Nome do Adicional',
            'preco': 'Preço do Adicional',
            'quantidade': 'Quantidade',
            'unidade': 'Unidade',
            'estado': 'Esta Ativo?',
            'descricao': 'Breve Descrição',
            'adicionalFornecedor': 'Fornecedores do Adicional',
        }
        widgets = {
            'nome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nome do Adicional',
                    'id': 'id_nome',
                    'maxlength': '100',
                    'name': 'nome',
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
            'quantidade': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'step': '0.00001',
                    'id': 'id_quantidade',
                    'name': 'quantidade',
                    'readonly':'readonly',
                }
            ),
            'unidade': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Unidade de Medida',
                    'id': 'id_unidade',
                    'maxlength': '3',
                    'name': 'unidade',
                    'readonly':'readonly',
                }
            ),
            'descricao': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Descrição do Adicional',
                    'id': 'id_descricao',
                    'name': 'descricao',
                    'readonly':'readonly',
                }
            ),
            'adicionalFornecedor': forms.SelectMultiple(
                attrs = {
                    'class': 'form-control',
                    'disabled':'disabled',
                }
            )
        }