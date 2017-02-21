# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0014_remove_rate_film_rel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
