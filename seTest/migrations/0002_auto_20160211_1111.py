# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seTest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]
