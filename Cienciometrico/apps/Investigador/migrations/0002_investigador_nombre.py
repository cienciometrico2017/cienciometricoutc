# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investigador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigador',
            name='Nombre',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]