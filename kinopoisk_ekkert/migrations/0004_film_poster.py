# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0003_film'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='poster',
            field=models.FileField(upload_to='', default=0),
        ),
    ]
