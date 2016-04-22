# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 13:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chart_account', '0002_remove_through_some'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartaccaunt',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='chartaccaunt',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date creation'),
        ),
        migrations.AlterField(
            model_name='chartaccaunt',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='chartaccaunt',
            name='number',
            field=models.CharField(max_length=255, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='chartaccaunt',
            name='through',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='through', to='chart_account.Through', verbose_name='Through'),
        ),
        migrations.AlterField(
            model_name='through',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='through',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date creation'),
        ),
        migrations.AlterField(
            model_name='through',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='through',
            name='number',
            field=models.CharField(max_length=255, verbose_name='Number'),
        ),
    ]