# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample_database', '0003_transfer_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='location',
        ),
    ]
