# -*- coding: utf-8 -*-

from datetime import datetime
from peewee import *

from application import DB
from models.category import Category


class Product(DB.Model):
    product_id = PrimaryKeyField()
    name = CharField(unique=True, null=False)
    price = FloatField(default=0, null=False)
    available_quantity = IntegerField(default=0, null=False)
    create_time = DateTimeField(default=datetime.now, null=False)

    category_id = ForeignKeyField(Category, to_field='category_id', null=False)

    class Meta:
        table_name = 'products'

    def __str__(self):
        return self.name
