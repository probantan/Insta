# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-22 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0008_auto_20190522_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='prof/'),
        ),
    ]
