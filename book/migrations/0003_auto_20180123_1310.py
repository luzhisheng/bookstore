# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='recipient_phone',
            field=models.CharField(verbose_name='手机号码', max_length=11),
        ),
    ]
