# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-20 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formacion_complementaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nivel_Estudios', models.CharField(max_length=50, null=True)),
                ('NombreTitulo', models.CharField(max_length=550, null=True)),
                ('Fecha_Fin', models.DateField(null=True)),
                ('Nombre_Centro_Estudios', models.CharField(max_length=250, null=True)),
            ],
            options={
                'permissions': (('ver_FormacionComplementaria', 'ver FormacionComplementaria'),),
            },
        ),
    ]
