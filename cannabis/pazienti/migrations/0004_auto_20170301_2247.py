# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pazienti', '0003_auto_20170226_0843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paziente',
            options={'ordering': ('num_paziente',), 'verbose_name': 'Paziente', 'verbose_name_plural': 'Pazienti'},
        ),
        migrations.AddField(
            model_name='paziente',
            name='luogo_nascita',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Luogo di nascita'),
        ),
    ]
