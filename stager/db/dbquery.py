from stager.db.dbconn import *

sysinf = system_information.sysinf()

dbquery = DatabaseQuery()

dbquery.create_json_table('system_information', sysinf)

dbquery.query_json_data('system_information')

