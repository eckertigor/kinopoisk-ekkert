# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0002_auto_20170216_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=49)),
                ('short_description', models.CharField(max_length=160)),
                ('full_description', models.CharField(max_length=750)),
                ('director', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('rating', models.IntegerField(default=0)),
                ('is_deleted', models.IntegerField(default=0)),
                ('add_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
