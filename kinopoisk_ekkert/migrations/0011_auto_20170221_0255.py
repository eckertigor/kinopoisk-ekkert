# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_ekkert', '0010_review_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='film',
            field=models.ForeignKey(to='kinopoisk_ekkert.Film'),
        ),
    ]
