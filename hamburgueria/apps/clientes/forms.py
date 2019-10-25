from django import forms
from .models import Cliente
from .choices import STATUS


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'rg', 'cpf', 'rua', 'bairro', 'cep', 'email', 'numeroCasa', 'telefone1', 'telefone2', 'celular1', 'celular2', 'foto', 'ativo', 'clienteCidade', 'clienteEstado', 'clientePais']
        labels = {
            'nome': 'Nome do Cliente',
            'sobrenome': 'Sobrenome do Cliente',
            'rg': 'RG',
            'cpf': 'CPF',
            'rua': 'Rua',
            'bairro': 'Bairro',
            'cep': 'CEP',
            'email': 'Email',
            'numeroCasa': 'Numero da Casa',
            'telefone1': 'Primeiro Telefone',
            'telefone2': 'Segundo Telefone',
            'celular1': 'Primeiro Celular',
            'celular2': 'Segundo Celular',
            'foto': 'Foto',
            'ativo': 'Esta Ativo?',
            'clienteCidade': 'Cidade',
            'clienteEstado': 'Estado',
            'clientePais': 'Pais',
        }
        widgets = {
            'nome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nome do Cliente',
                    'id': 'id_nome',
                    'maxlength': '100',
                    'name': 'nome'
                }
            ),
            'sobrenome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Sobrenome do Cliente',
                    'id': 'id_sobrenome',
                    'maxlength': '15',
                    'name': 'sobrenome'
                }
            ),
            'rg': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'RG',
                    'id': 'id_rg',
                    'maxlength': '12',
                    'name': 'rg'
                }
            ),
            'cpf': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'CPF',
                    'id': 'id_cpf',
                    'maxlength': '12',
                    'name': 'cpf'
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
            'numeroCasa': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '123456',
                    'id': 'id_numeroCasa',
                    'maxlength': '6',
                    'name': 'numeroCasa'
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

class ClienteFormReadonly(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'rg', 'cpf', 'rua', 'bairro', 'cep', 'email', 'numeroCasa', 'telefone1', 'telefone2', 'celular1', 'celular2', 'foto', 'ativo', 'clienteCidade', 'clienteEstado', 'clientePais']
        labels = {
            'nome': 'Nome do Cliente',
            'sobrenome': 'Sobrenome do Cliente',
            'rg': 'RG',
            'cpf': 'CPF',
            'rua': 'Rua',
            'bairro': 'Bairro',
            'cep': 'CEP',
            'email': 'Email',
            'numeroCasa': 'Numero da Casa',
            'telefone1': 'Primeiro Telefone',
            'telefone2': 'Segundo Telefone',
            'celular1': 'Primeiro Celular',
            'celular2': 'Segundo Celular',
            'foto': 'Foto',
            'ativo': 'Esta Ativo?',
            'clienteCidade': 'Cidade',
            'clienteEstado': 'Estado',
            'clientePais': 'Pais',
        }
        widgets = {
            'nome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nome do Cliente',
                    'id': 'id_nome',
                    'maxlength': '100',
                    'name': 'nome'
                }
            ),
            'sobrenome': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Sobrenome do Cliente',
                    'id': 'id_sobrenome',
                    'maxlength': '15',
                    'name': 'sobrenome'
                }
            ),
            'rg': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'RG',
                    'id': 'id_rg',
                    'maxlength': '12',
                    'name': 'rg'
                }
            ),
            'cpf': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'CPF',
                    'id': 'id_cpf',
                    'maxlength': '12',
                    'name': 'cpf'
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
            'numeroCasa': forms.TextInput(
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
        }