# Generated by Django 2.2.6 on 2019-10-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cidade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cidade',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]