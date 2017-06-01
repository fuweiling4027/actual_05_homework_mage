# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message2',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='message2',
            name='publish_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='message2',
            name='title',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='message2',
            name='username',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
