# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0012_auto_20170221_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='film_rel',
            field=models.ManyToManyField(to='kinopoisk_ekkert.Film'),
        ),
    ]
