# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=255)),
                ('pw_hash', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            managers=[
                ('userMgr', django.db.models.manager.Manager()),
            ],
        ),
    ]
