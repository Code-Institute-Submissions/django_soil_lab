# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-20 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('purpose', models.CharField(default='', max_length=254)),
                ('elements_determined', models.CharField(default='', max_length=254)),
                ('description', models.TextField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='images')),
                ('test_type', models.CharField(default='', max_length=254)),
            ],
        ),
    ]
