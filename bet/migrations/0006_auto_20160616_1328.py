# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0005_auto_20160616_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='final_result',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
