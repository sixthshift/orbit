# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=('pages.page', models.Model),
        ),
    ]
