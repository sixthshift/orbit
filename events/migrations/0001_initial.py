# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-09 15:38
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('group_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('version', models.IntegerField()),
                ('changelog', models.CharField(blank=True, max_length=50)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('timeframed', django.db.models.manager.Manager()),
            ],
        ),
    ]
