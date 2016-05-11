# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 11:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import mptt.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Unique code')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date creation')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=255, verbose_name='Full name')),
                ('number', models.CharField(max_length=255, verbose_name='Number')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('size', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Units')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['number'],
                'verbose_name': 'Product',
            },
        ),
        migrations.CreateModel(
            name='UnitsOfMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Unique code')),
                ('name', models.CharField(max_length=255, verbose_name='Full name')),
                ('short_name', models.CharField(max_length=255, verbose_name='Short name')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
            ],
            options={
                'verbose_name_plural': 'Units of measurements',
                'ordering': ['short_name'],
                'verbose_name': 'Units of measurement',
            },
        ),
        migrations.AlterModelOptions(
            name='productcatalog',
            options={'ordering': ['number'], 'verbose_name': 'Product Catalog', 'verbose_name_plural': 'Products Catalogs'},
        ),
        migrations.AlterField(
            model_name='productcatalog',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.ProductCatalog', verbose_name='Parent Catalog'),
        ),
        migrations.AddField(
            model_name='product',
            name='catalog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductCatalog', verbose_name='Catalog'),
        ),
        migrations.AddField(
            model_name='product',
            name='units',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.UnitsOfMeasurement', verbose_name='Units'),
        ),
    ]