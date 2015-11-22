# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foi_requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foirequest',
            name='title',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='foirequest',
            name='foi_text',
            field=models.TextField(verbose_name='Your FOI Request'),
        ),
    ]
