from django import forms
from .models import Ingrediente


class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nome', 'preco', 'quantidade', 'unidade', 'estado', 'descricao', 'ingredienteFornecedor']
        labels = {
            'nome': 'Nome do Ingrediente',
            'preco': 'Preço do Ingrediente',
            'quantidade': 'Quantidade',
            'unidade': 'Unidade',
            'estado': 'Esta Ativo?',
            'descricao': 'Breve Descrição',
            'ingredienteFornecedor': 'Fornecedores do Ingrediente',
        }
        widgets = {
            'nome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nome do Ingrediente',
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
                    'placeholder': 'Descrição do Ingrediente',
                    'id': 'id_descricao',
                    'name': 'descricao'
                }
            ),
            'ingredienteFornecedor': forms.SelectMultiple(
                attrs = {
                    'class': 'form-control',
                }
            )
        }

class IngredienteFormReadonly(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nome', 'preco', 'quantidade', 'unidade', 'estado', 'descricao', 'ingredienteFornecedor']
        labels = {
            'nome': 'Nome do Ingrediente',
            'preco': 'Preço do Ingrediente',
            'quantidade': 'Quantidade',
            'unidade': 'Unidade',
            'estado': 'Esta Ativo?',
            'descricao': 'Breve Descrição',
            'ingredienteFornecedor': 'Fornecedores do Ingrediente',
        }
        widgets = {
            'nome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nome do Ingrediente',
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
                    'placeholder': 'Descrição do Ingrediente',
                    'id': 'id_descricao',
                    'name': 'descricao',
                    'readonly':'readonly',
                }
            ),
            'ingredienteFornecedor': forms.SelectMultiple(
                attrs = {
                    'class': 'form-control',
                    'disabled':'disabled',
                }
            )
        }