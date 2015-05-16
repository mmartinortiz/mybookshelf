# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0003_book_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='nickname',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
