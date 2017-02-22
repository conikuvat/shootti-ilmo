# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-22 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoottikala', '0003_auto_20170210_2211'),
        ('event_log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='cosplayer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoottikala.Cosplayer'),
        ),
        migrations.AddField(
            model_name='entry',
            name='photographer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoottikala.Photographer'),
        ),
    ]
