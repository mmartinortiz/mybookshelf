# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_auto_20150503_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
