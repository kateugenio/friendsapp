# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 02:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myself', to='friends.User')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myfriend', to='friends.User')),
            ],
        ),
    ]