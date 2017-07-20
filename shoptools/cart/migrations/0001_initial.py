# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 13:29
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shoptools.cart.base
import shoptools.cart.util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('secret', models.UUIDField(db_index=True, default=shoptools.cart.util.make_uuid, editable=False)),
                ('_shipping_option', models.CharField(blank=True, db_column='shipping_option', default='', editable=False, max_length=255, verbose_name='shipping option')),
                ('_voucher_codes', models.TextField(blank=True, db_column='voucher_codes', default='', editable=False, verbose_name='voucher codes')),
                ('order_obj_id', models.PositiveIntegerField(null=True)),
                ('order_obj_content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, shoptools.cart.base.ICart, shoptools.cart.base.IShippable),
        ),
        migrations.CreateModel(
            name='SavedCartLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_object_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('quantity', models.IntegerField()),
                ('options', models.TextField(default='')),
                ('item_content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('parent_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.SavedCart')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, shoptools.cart.base.ICartLine),
        ),
        migrations.AlterUniqueTogether(
            name='savedcartline',
            unique_together=set([('item_content_type', 'item_object_id', 'parent_object', 'options')]),
        ),
    ]
