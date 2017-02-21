# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0009_auto_20170220_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user_avatar',
            field=models.CharField(max_length=30, default=0),
        ),
    ]
