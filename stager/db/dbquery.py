from .dbconn import *
from stager import system_information

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

# Selects all sysinf results (filtered by 'system_information' grouping
for result in systable.select().where(System.group == 'system_information'):
    print(result.property.title() + ": " + result.value)
