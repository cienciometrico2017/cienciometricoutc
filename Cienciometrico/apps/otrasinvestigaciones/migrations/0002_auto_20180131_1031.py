# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-31 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otrasinvestigaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otrasinvestigaciones',
            name='Documento',
            field=models.FileField(blank=True, null=True, upload_to='otrasinvestigaciones/'),
        ),
    ]
