# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-23 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0004_auto_20190223_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sampleresults',
            old_name='k_morgan_result',
            new_name='k',
        ),
        migrations.RenameField(
            model_name='sampleresults',
            old_name='lr_ph_result',
            new_name='lr_ph',
        ),
        migrations.RenameField(
            model_name='sampleresults',
            old_name='lab_comments',
            new_name='other_comments',
        ),
        migrations.RenameField(
            model_name='sampleresults',
            old_name='p_morgan_result',
            new_name='p',
        ),
        migrations.RenameField(
            model_name='sampleresults',
            old_name='ph_result',
            new_name='ph',
        ),
    ]