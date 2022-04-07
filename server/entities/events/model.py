
import peewee
from playhouse.postgres_ext import DateTimeTZField

from entities.event_chains.model import EventChain

class Event(peewee.Model):
    created_at = DateTimeTZField()
    path = peewee.CharField(max_length=1000)
    action = peewee.IntegerField() # 1: Open, 2: Close, 3: Away, 4: Back
    event_chain = peewee.ForeignKeyField(EventChain)
