# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('result', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('result', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Matches',
            new_name='Match',
        ),
        migrations.RemoveField(
            model_name='bets',
            name='match',
        ),
        migrations.RemoveField(
            model_name='bets',
            name='user',
        ),
        migrations.DeleteModel(
            name='Bets',
        ),
        migrations.AddField(
            model_name='result',
            name='match',
            field=models.ForeignKey(to='bet.Match'),
        ),
        migrations.AddField(
            model_name='bet',
            name='match',
            field=models.ForeignKey(to='bet.Match'),
        ),
        migrations.AddField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
