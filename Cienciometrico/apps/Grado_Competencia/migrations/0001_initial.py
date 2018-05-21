# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-20 14:20
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
            name='grado_competencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Valor', models.IntegerField()),
                ('investigador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador')),
            ],
        ),
    ]
