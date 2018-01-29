# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': '商品'},
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(upload_to='book', verbose_name='商品图片'),
        ),
        migrations.AlterModelTable(
            name='books',
            table='books',
        ),
    ]
