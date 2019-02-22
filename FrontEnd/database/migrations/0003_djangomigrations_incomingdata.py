# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-22 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IncomingData',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('type', models.TextField(blank=True, null=True)),
                ('total_heartbeats', models.IntegerField(blank=True, null=True)),
                ('client_ip', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Incoming_Data',
                'managed': False,
            },
        ),
    ]
