# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0002_auto_20160610_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='round',
            field=models.CharField(max_length=2, choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five'), ('6', 'six')], default='1'),
        ),
    ]
