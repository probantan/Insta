# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-22 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0007_auto_20190522_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pic/'),
        ),
    ]