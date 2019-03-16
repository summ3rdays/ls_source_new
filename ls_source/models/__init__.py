# -*- coding: utf-8 -*-


def init_models(db):

    from models.category import Category
    from models.customer import Customer
    from models.order import Order, OrderItem
    from models.product import Product


    ms = [Category, Product, Customer, Order, OrderItem, Customer]

    db.database.create_tables(ms)