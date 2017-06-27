# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 01:08
from __future__ import unicode_literals

from django.db import migrations, models
import shoptools.cart.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            bases=(models.Model, shoptools.cart.base.ICartItem),
        ),
    ]