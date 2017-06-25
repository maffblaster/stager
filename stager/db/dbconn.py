# Connects to SQLite database
from peewee import *
from stager import system_information
from playhouse.sqlite_ext import SqliteDatabase
import datetime

db = SqliteDatabase('gentoo_data.db')

class BaseModel(Model):
    class Meta:
        database = db


class System(BaseModel):
    group = TextField()
    property = TextField()
    value = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)


class GentooConfig(BaseModel):
    group = TextField()
    property = TextField()
    value = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)


sysinf = system_information.sysinf()

db.connect()

db.drop_table(System)
db.drop_table(GentooConfig)

db.create_table(System)
db.create_table(GentooConfig)

systable = System()
gentootable = GentooConfig()

# Inserts all sysinf attributes into sqlite database
for attr, value in sysinf.__dict__.items():
    systable.create(group='system_information', property=attr, value=value)

# Selects all sysinf results (filtered by 'system_information' grouping) from sqlite database
for result in systable.select().where(System.group == 'system_information'):
    print(result.property.title() + ": " + result.value)
