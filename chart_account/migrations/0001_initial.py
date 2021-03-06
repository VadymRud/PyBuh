# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 13:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChartAccaunt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(default=uuid.uuid4, verbose_name='Unique code')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата Создания')),
                ('active', models.BooleanField(default=True, verbose_name='Активный')),
                ('name', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('number', models.CharField(max_length=255, verbose_name='Полное имя')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Through',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(default=uuid.uuid4, verbose_name='Unique code')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата Создания')),
                ('active', models.BooleanField(default=True, verbose_name='Активный')),
                ('name', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('number', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('some', models.CharField(max_length=100, verbose_name='Полное имя')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='chartaccaunt',
            name='through',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='through___qqq', to='chart_account.Through'),
        ),
    ]
