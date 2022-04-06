
import peewee

class Session(peewee.Model):
    start = peewee.DateTimeField()
    end = peewee.DateTimeField()
