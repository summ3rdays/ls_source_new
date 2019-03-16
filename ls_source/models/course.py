from datetime import datetime
from peewee import *

from application import DB
from models.specialization import Specialization
from models.provider import Provider


class Course(DB.Model):
    course_id = PrimaryKeyField()
    name = CharField(100, null=False)
    price = FloatField(default=0, null=False)
    #p_id = ForeignKeyField(Provider, to_field='id')
    spec= ForeignKeyField(Specialization, to_field= 'spec_id')
    creation_date = DateTimeField(default=datetime.now, null=False)
    is_active = BooleanField(default=True)

    class Meta:
        table_name = 'courses'

    def __str__(self):
        return self.name