# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fio',
            field=models.CharField(max_length=50),
        ),
    ]
