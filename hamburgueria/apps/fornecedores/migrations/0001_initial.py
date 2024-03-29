# Generated by Django 2.2.6 on 2019-10-23 20:24

import apps.fornecedores.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estado', '0001_initial'),
        ('pais', '0001_initial'),
        ('cidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('idFornecedor', models.AutoField(primary_key=True, serialize=False)),
                ('razao_social', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=15)),
                ('ie', models.CharField(max_length=12)),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=100)),
                ('numeroLocal', models.CharField(max_length=6)),
                ('telefone1', models.CharField(max_length=24)),
                ('telefone2', models.CharField(max_length=24)),
                ('celular1', models.CharField(max_length=24)),
                ('celular2', models.CharField(max_length=24)),
                ('foto', models.ImageField(default='sem-imagem-avatar.png', upload_to=apps.fornecedores.models.user_directory_path)),
                ('ativo', models.CharField(choices=[('yes', 'sim'), ('no', 'não')], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fornecedorCidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cidade.Cidade')),
                ('fornecedorEstado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estado.Estado')),
                ('fornecedorPais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pais.Pais')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
                'ordering': ['razao_social'],
            },
        ),
    ]
