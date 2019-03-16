from datetime import datetime
from peewee import *

from application import DB
from models.course import Course


class Schedule(DB.Model):

    id = PrimaryKeyField()
    c_id = ForeignKeyField(Course, to_field='id', null=False)
    start_date = DateTimeField(default=datetime.now, null=False)
    end_date = DateTimeField(default=None)


    class Meta:
        table_name = 'schedule'

    def __unicode__(self):
        return '%s %s' % (self.sch_id, self.sch_name)

    def __str__(self):
        return '%s %s' % (self.sch_id, self.sch_name)