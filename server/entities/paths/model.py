
import peewee

from entities.domains.model import Domain

class Path(peewee.Model):
    created_at = peewee.DateTimeField()
    path = peewee.CharField(max_length=1000)
    domain = peewee.ForeignKeyField(Domain)
