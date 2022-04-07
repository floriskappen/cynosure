
import peewee
from playhouse.postgres_ext import DateTimeTZField

class Domain(peewee.Model):
    created_at = DateTimeTZField()
    domain = peewee.CharField()

