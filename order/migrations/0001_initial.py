# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180125_0803'),
        ('book', '0003_auto_20180123_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('is_delete', models.BooleanField(verbose_name='逻辑删除', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('count', models.DecimalField(verbose_name='商品价格', max_digits=10, decimal_places=2)),
                ('price', models.DecimalField(verbose_name='商品价格', max_digits=12, decimal_places=2)),
                ('books', models.ForeignKey(verbose_name='订单商品', to='books.Books')),
            ],
            options={
                'verbose_name': '订单商品',
                'db_table': 'ordergoods',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('is_delete', models.BooleanField(verbose_name='逻辑删除', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('order_id', models.CharField(max_length=64, verbose_name='订单编号', serialize=False, primary_key=True)),
                ('total_count', models.IntegerField(verbose_name='商品总数', default=1)),
                ('total_price', models.DecimalField(verbose_name='商品总价', max_digits=10, decimal_places=2)),
                ('transit_price', models.DecimalField(verbose_name='订单运费', max_digits=10, decimal_places=2)),
                ('pay_method', models.SmallIntegerField(verbose_name='支付方式', default=1, choices=[(1, '货到付款'), (2, '微信支付'), (3, '支付宝'), (4, '银联支付')])),
                ('status', models.SmallIntegerField(verbose_name='订单状态', default=1, choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成')])),
                ('trade_id', models.CharField(max_length=100, verbose_name='支付编号', unique=True, blank=True, null=True)),
                ('addr', models.ForeignKey(verbose_name='收货地址', to='book.Address')),
                ('passport', models.ForeignKey(verbose_name='下单账户', to='book.Passport')),
            ],
            options={
                'verbose_name': '订单信息',
                'db_table': 'orderInfo',
            },
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(verbose_name='所属订单id', to='order.OrderInfo'),
        ),
    ]
