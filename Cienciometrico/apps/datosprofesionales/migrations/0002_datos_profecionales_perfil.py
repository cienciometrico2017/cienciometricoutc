# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.7 on 2018-05-10 21:34
=======
# Generated by Django 1.11.7 on 2018-05-13 20:20
>>>>>>> 190d19e7efff91de1d19fc35b9343adb30edf859
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfiles', '0001_initial'),
        ('datosprofesionales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_profecionales',
            name='perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfiles.Perfil'),
        ),
    ]
