from datetime import datetime
from peewee import *

from application import DB


class Provider(DB.Model):

    prov_id = PrimaryKeyField()
    name = CharField(50, null=False)
    email = CharField(30)
    phone = CharField(21)
    creation_date = DateTimeField(default=datetime.now, null=False)

    class Meta:
        table_name = 'providers'

    def __unicode__(self):
        return '%s %s' % (self.provider_id, self.provider_name)

    def __str__(self):
        return '%s %s' % (self.provider_id, self.provider_name)