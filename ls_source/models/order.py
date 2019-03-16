# -*- coding: utf-8 -*-

from datetime import datetime
from peewee import *

from application import DB
from models.customer import Customer

STATUSES = [(1, 'Pre-Order'),
            (2, 'Payment'),
            (3, 'Paid'),
            (4, 'Formation'),
            (5, 'Delivery'),
            (6, 'Performed')]


class Order(DB.Model):

    order_id = PrimaryKeyField()
    customer_id = ForeignKeyField(Customer, to_field='customer_id', null=False)
    order_status = CharField(choices=STATUSES, null=False)
    create_time = DateTimeField(default=datetime.now, null=False)

    class Meta:
        table_name = 'orders'

class OrderItem(DB.Model):

    item_id = PrimaryKeyField()
    order_id = ForeignKeyField(Order, to_field='order_id', null=False, on_delete='CASCADE')
   # product_id = ForeignKeyField(Product, to_field='product_id', null=False)
    list_price = FloatField(default=0, null=False)
    quantity = IntegerField(default=0, null=False)

    class Meta:
        table_name = 'order_items'
