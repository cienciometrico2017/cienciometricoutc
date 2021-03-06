# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-07 19:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfiles', '0001_initial'),
        ('roles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='roles',
            field=models.ManyToManyField(to='roles.Rol'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
