# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20171118_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='stock'),
        ),
    ]
