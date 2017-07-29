# Connects to SQLite database
from peewee import *
from stager import system_information
from playhouse.sqlite_ext import SqliteDatabase, JSONField
import datetime
import json

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

class JsonData(BaseModel):
    datakey = TextField()
    datastring = TextField()


class DatabaseQuery():

    db.connect()

    def create_json_table(self, key, data):

        json_table = JsonData()

        json_data = json.dumps(data, default=lambda data: data.__dict__)

        if json_table.table_exists():
            # Drops and re-creates table. Should be re-written as an update statement
            json_table.drop_table()
            db.create_table(json_table, True)
            json_table.create(datakey=key, datastring=json_data)

        else:
            db.create_table(json_table, True)
            json_table.create(datakey=key, datastring=json_data)


    def query_json_data(self, key):

        for result in JsonData.select().where(JsonData.datakey == key):
            print(result.datakey + ": " + result.datastring)


''' 
    def create_config_table(self):
        
    def query_config_table(self):


db.drop_table(System)
db.drop_table(GentooConfig)

db.create_table(System)
db.create_table(GentooConfig)

systable = System()
gentootable = GentooConfig()

'''

'''
# Inserts all sysinf attributes into sqlite database
for attr, value in sysinf.__dict__.items():
    systable.create(group='system_information', property=attr, value=value)

# Selects all sysinf results (filtered by 'system_information' grouping) from sqlite database
for result in systable.select().where(System.group == 'system_information'):
    print(result.property.title() + ": " + result.value)
'''

