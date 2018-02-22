# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20180222_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Has been published?'),
        ),
        migrations.AlterField(
            model_name='question',
            name='html',
            field=models.TextField(verbose_name='Question Text'),
        ),
    ]