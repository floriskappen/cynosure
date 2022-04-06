
import peewee

from entities.paths.model import Path
from entities.sessions.model import Session

class Event(peewee.Model):
    created_at = peewee.DateTimeField()
    duration = peewee.IntegerField()
    path = peewee.ForeignKeyField(Path)
    # session = peewee.ForeignKeyField(Session)
