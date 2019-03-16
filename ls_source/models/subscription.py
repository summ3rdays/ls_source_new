from datetime import datetime
from peewee import *

from application import DB
from models.student import Student
from models.course import Course


class Subscription(DB.Model):
    id = PrimaryKeyField()
    s_id = ForeignKeyField(Student, to_field='id', null=False, on_delete='CASCADE')
    c_id = ForeignKeyField(Course, to_field='id', null=False)
    start_date = DateTimeField(default=datetime.now, null=False)
    end_date = DateTimeField(default=None)

    class Meta:
        table_name = 'subscriptions'
