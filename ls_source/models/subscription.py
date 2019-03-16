from datetime import datetime
from peewee import *

from application import DB
from models.student import Student
from models.course import Course


class Subscription(DB.Model):
    id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field='student_id', null=False, on_delete='CASCADE')
    course_id = ForeignKeyField(Course, to_field='course_id', null=False)
    start_date = DateTimeField(default=datetime.now, null=False)
    end_date = DateTimeField(default=None)

    class Meta:
        table_name = 'subscriptions'
