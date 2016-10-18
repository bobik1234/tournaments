# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0006_auto_20160616_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='final_result',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team2',
        ),
        migrations.AddField(
            model_name='match',
            name='away_goals',
            field=models.DecimalField(null=True, decimal_places=0, blank=True, max_digits=2),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=django_countries.fields.CountryField(max_length=2, default=datetime.datetime(2016, 6, 17, 9, 10, 29, 597256, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='home_goals',
            field=models.DecimalField(null=True, decimal_places=0, blank=True, max_digits=2),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=django_countries.fields.CountryField(max_length=2, default=22),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='match_date',
            field=models.DateTimeField(null=True, verbose_name='match date', blank=True),
        ),
    ]
