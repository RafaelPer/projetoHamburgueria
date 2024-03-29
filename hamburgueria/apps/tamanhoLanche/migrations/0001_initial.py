# Generated by Django 2.2.6 on 2019-10-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tamanhoLanche',
            fields=[
                ('idTamanhoLanche', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'tamanhoLanche',
                'verbose_name_plural': 'tamanhosLanches',
                'ordering': ['nome'],
            },
        ),
    ]
