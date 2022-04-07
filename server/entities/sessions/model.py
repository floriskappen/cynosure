
import peewee
from playhouse.postgres_ext import DateTimeTZField

class Session(peewee.Model):
    created_at = DateTimeTZField()
