
import peewee

class Domain(peewee.Model):
    domain = peewee.CharField()
    created_at = peewee.DateTimeField()

