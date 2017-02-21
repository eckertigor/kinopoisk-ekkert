# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0013_rate_film_rel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='film_rel',
        ),
    ]
