# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-19 12:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0008_auto_20190218_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultsLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_morgan_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('k_morgan_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('lr_ph_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('ph_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('mg_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('cu_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('zn_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('er_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('mn_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('organic_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sample',
            name='customer_ref',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='location',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='site_address',
        ),
        migrations.AddField(
            model_name='sample',
            name='batch_no',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='customer_name',
            field=models.CharField(blank=True, help_text='Name of customer e.g. Tom Cronin', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='customer_ref_1',
            field=models.CharField(blank=True, help_text='Customer site primary reference e.g. Tom Cronins Main Farm', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='customer_ref_2',
            field=models.CharField(blank=True, help_text='Customer site secondary reference e.g. South field', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='recieved_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='sample_address',
            field=models.CharField(blank=True, help_text='Address of the sample site.', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='sample_location',
            field=geoposition.fields.GeopositionField(help_text='Drag the marker to pin the location of the sample site.', max_length=42, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='tested_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='analysis_req',
            field=models.CharField(choices=[('1', 'Soil 1-SS Basic'), ('2', 'Soil 2-SS Dairy/Beef/Sheep/Horses'), ('3', 'Soil 3-SS Sheep/Tillage'), ('4', 'Soil 4-SS Tillage'), ('5', 'Soil 5-SS Horticulture'), ('6', 'Soil 6-SS Tillage/Grassland (S1 + Mg)'), ('7', 'Soil 7-SS Organic Matter'), ('8', 'Soil 8-SS Tillage (S6 + S7)'), ('9', 'Soil 9-SS Tillage (S4 + S7)')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sample_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sample_ref',
            field=models.CharField(help_text='Sample reference number assigned by lab, e.g. SS-123456', max_length=50),
        ),
        migrations.AlterField(
            model_name='sample',
            name='submit_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultslineitem',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.Sample'),
        ),
    ]