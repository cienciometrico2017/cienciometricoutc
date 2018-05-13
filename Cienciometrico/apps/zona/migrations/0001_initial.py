# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-13 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=150)),
                ('Descripcion', models.TextField()),
                ('pais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pais.pais')),
            ],
            options={
                'permissions': (('ver_zona', 'ver zona'),),
            },
        ),
    ]
