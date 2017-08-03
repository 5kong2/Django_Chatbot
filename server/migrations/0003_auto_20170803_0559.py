# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-03 05:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20170803_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AlterField(
            model_name='member',
            name='nickname',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AlterField(
            model_name='member',
            name='url',
            field=models.TextField(default='', validators=[django.core.validators.URLValidator()]),
        ),
    ]