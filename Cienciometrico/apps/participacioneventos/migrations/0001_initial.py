# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-18 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='participacionevento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=255)),
                ('Nivel_Autoria', models.CharField(max_length=255)),
                ('Palabras_Clave', models.TextField(max_length=550)),
                ('Resumen', models.TextField(max_length=550)),
                ('Documento', models.FileField(blank=True, null=True, upload_to='eventos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('Nombre_Evento', models.CharField(max_length=255)),
                ('Nivel', models.CharField(max_length=255)),
                ('Lugar_Evento', models.CharField(max_length=255)),
                ('Fecha_Evento', models.DateField()),
            ],
            options={
                'permissions': (('ver_ParticipacionesEventos', 'ver ParticipacionesEventos'),),
            },
        ),
    ]
