# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-19 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articulos_cientificos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('Resumen', models.CharField(blank=True, max_length=250, null=True)),
                ('PalabrasClaves', models.CharField(blank=True, max_length=250, null=True)),
                ('Documento', models.FileField(null=True, upload_to='articulos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('NombreRevista', models.CharField(blank=True, max_length=250, null=True)),
                ('Volumen', models.CharField(blank=True, max_length=250, null=True)),
                ('Numero', models.CharField(blank=True, max_length=250, null=True)),
                ('ISSN', models.CharField(blank=True, max_length=250, null=True)),
                ('Base_Datos', models.CharField(blank=True, max_length=250, null=True)),
                ('Url', models.URLField(blank=True, null=True)),
                ('Fecha_Publicacion', models.DateField(blank=True, null=True)),
            ],
            options={
                'permissions': (('ver_articulo', 'ver articulo'),),
            },
        ),
    ]