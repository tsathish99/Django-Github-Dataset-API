# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-19 10:54
from __future__ import unicode_literals

import RestAPI.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('created', RestAPI.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', RestAPI.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=50)),
                ('avatar_url', models.URLField()),
                ('event_count', models.IntegerField(default=0)),
                ('latest_event_timestamp', models.DateTimeField()),
                ('streak', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-event_count', 'latest_event_timestamp', 'login'),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created', RestAPI.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', RestAPI.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=12)),
                ('created_at', models.DateTimeField()),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestAPI.Actor')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('created', RestAPI.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', RestAPI.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestAPI.Repo'),
        ),
    ]