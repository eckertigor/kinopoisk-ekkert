# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0011_auto_20170221_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='film',
            field=models.IntegerField(),
        ),
    ]
