from datetime import datetime
from peewee import *

from application import DB


class Student(DB.Model):

    s_id = PrimaryKeyField()
    s_first_name = CharField(50, null=False)
    s_last_name = CharField(50, null=False)
    s_email = CharField(unique=True, null=False)
    s_phone = CharField(21, unique=True, null=False)
    s_birthday = DateField(null=True)
    s_creation_date = DateTimeField(default=datetime.now, null=False)
    s_is_active = BooleanField(default=True)

    class Meta:
        table_name = 'students'

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)