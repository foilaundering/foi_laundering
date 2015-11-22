# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import foi_requests.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('slug', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FOIRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('foi_text', models.TextField()),
                ('make_live_date', models.DateTimeField(default=foi_requests.models.random_date_in_future)),
                ('sent', models.BooleanField(default=False)),
                ('receiving_authority', models.ForeignKey(to='foi_requests.Authority')),
            ],
        ),
    ]
