# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0004_film_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
