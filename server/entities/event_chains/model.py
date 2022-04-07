
import peewee
from playhouse.postgres_ext import DateTimeTZField

from entities.domains.model import Domain
from entities.sessions.model import Session

class EventChain(peewee.Model):
    created_at = DateTimeTZField()
    domain = peewee.ForeignKeyField(Domain)
    session = peewee.ForeignKeyField(Session)
    last_ping = DateTimeTZField()
    is_closed = peewee.BooleanField(default=False)

