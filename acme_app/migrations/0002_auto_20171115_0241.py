# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-14 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='city',
            field=models.CharField(default='Jaipur', max_length=240),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='email',
            field=models.EmailField(max_length=240),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='phno',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='pin',
            field=models.CharField(max_length=240),
        ),
    ]