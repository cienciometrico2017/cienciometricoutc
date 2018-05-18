# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-10 21:34
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='intereses_formativos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tematicaInteres', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='SintaxisInvalida', message='Solo letras', regex='^[a-zA-Z]*$')])),
                ('descripcion', models.TextField(max_length=50)),
                ('palabrasClave', models.CharField(max_length=300)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('ver_interes', 'ver interes'),),
            },
        ),
    ]
