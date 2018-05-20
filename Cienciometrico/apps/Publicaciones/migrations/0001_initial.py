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
            name='publicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=500)),
                ('NombrePublica', models.TextField(null=True)),
                ('UbicacionFisica', models.TextField(null=True)),
                ('Url', models.URLField(null=True)),
            ],
            options={
                'permissions': (('ver_Publicaciones', 'ver Publicaciones'),),
            },
        ),
    ]
