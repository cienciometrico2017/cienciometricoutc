# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-18 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zona', '0001_initial'),
        ('pais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=155)),
                ('pais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pais.pais')),
                ('zona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zona.zona')),
            ],
            options={
                'permissions': (('ver_provincia', 'ver provincia'),),
            },
        ),
    ]
