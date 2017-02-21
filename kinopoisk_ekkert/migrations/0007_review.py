# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import kinopoisk_ekkert.models


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0006_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user', models.CharField(max_length=30)),
                ('film', models.IntegerField(verbose_name=kinopoisk_ekkert.models.Film)),
                ('text', models.CharField(max_length=500)),
            ],
        ),
    ]
