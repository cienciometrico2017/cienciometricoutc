# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-07 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Investigador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bitacora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hora', models.DateTimeField()),
                ('Fecha', models.DateField()),
                ('Actividades', models.TextField(max_length=100)),
                ('investigador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador')),
            ],
        ),
    ]
