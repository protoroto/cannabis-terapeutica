# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pazienti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventiavversi',
            name='sonnolenza_sedazione',
            field=models.BooleanField(default=False, verbose_name='Sonnolenza, sedazione'),
        ),
        migrations.AlterField(
            model_name='eventiavversi',
            name='sonnolenza',
            field=models.BooleanField(default=False, verbose_name='Sonnolenza'),
        ),
    ]
