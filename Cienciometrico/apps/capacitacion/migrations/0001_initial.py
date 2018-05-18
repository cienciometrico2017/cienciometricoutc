# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-10 21:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='capacitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaConocimiento', models.CharField(max_length=350)),
                ('horas', models.IntegerField()),
                ('institucion', models.CharField(max_length=350)),
                ('descripcion', models.CharField(max_length=350)),
                ('evidencias', models.FileField(blank=True, null=True, upload_to='capacitaciones/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('ver_capacitacion', 'ver capacitación'),),
            },
        ),
    ]
