# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recall', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='user',
        ),
    ]
