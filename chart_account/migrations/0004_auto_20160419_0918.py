# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 09:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chart_account', '0003_auto_20160418_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartAccauntGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Unique code')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date creation')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=255, verbose_name='Full name')),
                ('number', models.CharField(max_length=255, verbose_name='Number')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='chartaccaunt',
            name='through',
        ),
        migrations.AddField(
            model_name='chartaccaunt',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='chartaccaunt',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Unique code'),
        ),
        migrations.DeleteModel(
            name='Through',
        ),
        migrations.AddField(
            model_name='chartaccaunt',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='through', to='chart_account.ChartAccauntGroup', verbose_name='Group Accaunt'),
        ),
    ]