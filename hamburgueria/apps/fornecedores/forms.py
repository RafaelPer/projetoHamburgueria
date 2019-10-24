from django import forms
from .models import Fornecedor
from .choices import STATUS


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['razao_social', 'cnpj', 'ie', 'rua', 'bairro', 'cep', 'email', 'numeroLocal', 'telefone1', 'telefone2', 'celular1', 'celular2', 'foto', 'ativo', 'fornecedorCidade', 'fornecedorEstado', 'fornecedorPais']
        labels = {
            'razao_social': 'Razão Social do Fornecedor',
            'cnpj': 'CNPJ',
            'ie': 'IE',
            'rua': 'Rua',
            'bairro': 'Bairro',
            'cep': 'CEP',
            'email': 'Email',
            'numeroLocal': 'Numero do Local',
            'telefone1': 'Primeiro Telefone',
            'telefone2': 'Segundo Telefone',
            'celular1': 'Primeiro Celular',
            'celular2': 'Segundo Celular',
            'foto': 'Foto',
            'ativo': 'Esta Ativo?',
            'fornecedorCidade': 'Cidade',
            'fornecedorEstado': 'Estado',
            'fornecedorPais': 'Pais',
        }
        widgets = {
            'razao_social': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Razão Social',
                    'id': 'id_razao_social',
                    'maxlength': '100',
                    'name': 'razao_social'
                }
            ),
            'cnpj': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'CNPJ',
                    'id': 'id_cnpj',
                    'maxlength': '15',
                    'name': 'cnpj'
                }
            ),
            'ie': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'IE',
                    'id': 'id_ie',
                    'maxlength': '12',
                    'name': 'ie'
                }
            ),
            'rua': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Rua',
                    'id': 'id_rua',
                    'maxlength': '100',
                    'name': 'rua'
                }
            ),
            'bairro': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Bairro',
                    'id': 'id_bairro',
                    'maxlength': '100',
                    'name': 'bairro'
                }
            ),
            'cep': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'CEP',
                    'id': 'id_cep',
                    'maxlength': '100',
                    'name': 'cep'
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'tesste@hotmail.com',
                    'id': 'id_email',
                    'maxlength': '100',
                    'name': 'email'
                }
            ),            
            'numeroLocal': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '123456',
                    'id': 'id_numeroLocal',
                    'maxlength': '6',
                    'name': 'numeroLocal'
                }
            ),
            'telefone1': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Telefone',
                    'id': 'id_telefone1',
                    'maxlength': '24',
                    'name': 'telefone1'
                }
            ),
            'telefone2': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'segundo telefone',
                    'id': 'id_telefone2',
                    'maxlength': '24',
                    'name': 'telefone2'
                }
            ),
            'celular1': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Celular',
                    'id': 'id_celular1',
                    'maxlength': '24',
                    'name': 'celular1'
                }
            ),
            'celular2': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'segundo celular',
                    'id': 'id_celular2',
                    'maxlength': '24',
                    'name': 'celular2'
                }
            ),

        }

class FornecedorFormReadonly(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['razao_social', 'cnpj', 'ie', 'rua', 'bairro', 'cep', 'email', 'numeroLocal', 'telefone1', 'telefone2', 'celular1', 'celular2', 'foto', 'ativo', 'fornecedorCidade', 'fornecedorEstado', 'fornecedorPais']
        labels = {
            'razao_social': 'Razão Social do Fornecedor',
            'cnpj': 'CNPJ',
            'ie': 'IE',
            'rua': 'Rua',
            'bairro': 'Bairro',
            'cep': 'CEP',
            'email': 'Email',
            'numeroLocal': 'Numero do Local',
            'telefone1': 'Primeiro Telefone',
            'telefone2': 'Segundo Telefone',
            'celular1': 'Primeiro Celular',
            'celular2': 'Segundo Celular',
            'foto': 'Foto',
            'ativo': 'Esta Ativo?',
            'fornecedorCidade': 'Cidade',
        }
        widgets = {
            'razao_social': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Razão Social',
                    'id': 'id_razao_social',
                    'maxlength': '100',
                    'name': 'razao_social',
                    'readonly':'readonly',
                }
            ),
            'cnpj': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'CNPJ',
                    'id': 'id_cnpj',
                    'maxlength': '15',
                    'name': 'cnpj',
                    'readonly':'readonly',
                }
            ),
            'ie': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'IE',
                    'id': 'id_ie',
                    'maxlength': '12',
                    'name': 'ie',
                    'readonly':'readonly',
                }
            ),
            'rua': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Rua',
                    'id': 'id_rua',
                    'maxlength': '100',
                    'name': 'rua',
                    'readonly':'readonly',
                }
            ),
            'bairro': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Bairro',
                    'id': 'id_bairro',
                    'maxlength': '100',
                    'name': 'bairro',
                    'readonly':'readonly',
                }
            ),
            'cep': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'CEP',
                    'id': 'id_cep',
                    'maxlength': '100',
                    'name': 'cep',
                    'readonly':'readonly',
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'tesste@hotmail.com',
                    'id': 'id_email',
                    'maxlength': '100',
                    'name': 'email',
                    'readonly':'readonly',
                }
            ),            
            'numeroLocal': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '123456',
                    'id': 'id_numeroLocal',
                    'maxlength': '6',
                    'name': 'numeroLocal',
                    'readonly':'readonly',
                }
            ),
            'telefone1': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Telefone',
                    'id': 'id_telefone1',
                    'maxlength': '24',
                    'name': 'telefone1',
                    'readonly':'readonly',
                }
            ),
            'telefone2': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'segundo telefone',
                    'id': 'id_telefone2',
                    'maxlength': '24',
                    'name': 'telefone2',
                    'readonly':'readonly',
                }
            ),
            'celular1': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Celular',
                    'id': 'id_celular1',
                    'maxlength': '24',
                    'name': 'celular1',
                    'readonly':'readonly',
                }
            ),
            'celular2': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'segundo celular',
                    'id': 'id_celular2',
                    'maxlength': '24',
                    'name': 'celular2',
                    'readonly':'readonly',
                }
            ),
            'foto': forms.ImageField(
                required=True,
                widget=forms.FileInput(
                    attrs= {
                        'class': 'custom-file-input',
                        'id': 'id_foto',
                        'name': 'foto',
                        'disabled': 'disabled',
                    }
                )
            ),
            'ativo': forms.MultipleChoiceField(
                choices=STATUS,
                required=True,
                widget=forms.CheckboxSelectMultiple(
                    attrs = {
                        'class': 'custom-select',
                        'id': 'id_ativo',
                        'maxlength': '5',
                        'name': 'ativo',
                        'disabled': 'disabled',
                    },
                ),
            ),
        }