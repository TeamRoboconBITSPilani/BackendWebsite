# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-04 08:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 4, 8, 2, 20, 183372, tzinfo=utc)),
        ),
    ]
