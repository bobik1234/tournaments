# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0003_match_round'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bet',
            old_name='result',
            new_name='expected_result',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='result',
            new_name='final_result',
        ),
    ]
