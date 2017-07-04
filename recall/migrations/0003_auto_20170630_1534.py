# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-30 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recall', '0002_remove_schedule_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=30, unique=True, verbose_name='Card Number')),
                ('patient_name', models.CharField(help_text='Title Surname Firstname', max_length=50, verbose_name='Patient Name')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7, verbose_name='Sex')),
                ('date_of_birth', models.DateField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>', verbose_name='Date of Birth')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Address')),
                ('occupation', models.CharField(blank=True, max_length=50, verbose_name='Occupation')),
                ('hmo', models.CharField(blank=True, help_text='Name of HMO(HMO ID Number)', max_length=100, verbose_name='HMO')),
            ],
            options={
                'ordering': ['card_number'],
            },
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date_of_recall',
            field=models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>', verbose_name='Date of Recall'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date_of_visit',
            field=models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>', verbose_name='Date of Visit'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='patient',
            field=models.CharField(help_text='Title Surname Firstname', max_length=50, verbose_name='Patient Name'),
        ),
    ]