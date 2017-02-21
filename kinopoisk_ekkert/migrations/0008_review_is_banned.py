# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0007_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_banned',
            field=models.IntegerField(default=0),
        ),
    ]
