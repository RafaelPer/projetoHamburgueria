from django import forms
from .models import tipoFuncionario


class TipoFuncionarioForm(forms.ModelForm):
    class Meta:
        model = tipoFuncionario
        fields = ['nome', 'descricao', 'estado']
        labels = {
            'nome': 'Nome do Tipo de Funcionario',
            'descrição': 'Breve Descrição',
            'estado': 'Esta Ativo?',
        }
        widgets = {
            'nome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nome do Tipo de Usuario',
                    'id': 'id_nome',
                    'maxlength': '100',
                    'name': 'nome'
                }
            ),
            'descricao': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Descrição do Tipo de Usuario',
                    'id': 'id_descricao',
                    'name': 'descricao'
                }
            ),

        }

class TipoFuncionarioFormReadonly(forms.ModelForm):
    class Meta:
        model = tipoFuncionario
        fields = ['nome', 'descricao', 'estado']
        labels = {
            'nome': 'Nome do Tipo de Funcionario',
            'descrição': 'Breve Descrição',
            'estado': 'Esta Ativo?',
        }
        widgets = {
            'nome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nome do Tipo de Usuario',
                    'id': 'id_nome',
                    'maxlength': '100',
                    'name': 'nome',
                    'readonly':'readonly',
                }
            ),
            'descricao': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Descrição do Tipo de Usuario',
                    'id': 'id_descricao',
                    'name': 'descricao',
                    'readonly':'readonly',
                }
            ),
        }