# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170826_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile_image',
            field=models.ImageField(default='static/car1.jpg', upload_to='static/media/'),
        ),
    ]
