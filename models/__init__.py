import os
from peewee import Model
from playhouse.sqlite_ext import SqliteExtDatabase


class BaseModel(Model):
    class Meta:
        h = os.getenv("XDG_DATA_HOME")
        database = SqliteExtDatabase(f"{h}database.db")
