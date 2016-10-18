# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0004_auto_20160613_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='match',
        ),
        migrations.AddField(
            model_name='match',
            name='final_result',
            field=models.CharField(max_length=200, default=None),
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
