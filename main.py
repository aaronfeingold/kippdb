from services.dbconn import GetDatabaseConnection
from services.dbsearcher import DbSearcher

def run():
  dbc = GetDatabaseConnection()
  dbs = DbSearcher(dbc)
  tables_list = dbs.list_table_names_from_db()
  result_list = []
  for db_object_name in sorted(tables_list):
    print(db_object_name)
    obj = dict()
    associated_views = dbs.find(source=db_object_name, targets="views")
    associated_triggers = dbs.find(source=db_object_name, targets="triggers")
    associated_stored_procedures = dbs.find(source=db_object_name, targets="stored_procedures")
    result = {
      "views": associated_views,
      "triggers": associated_triggers,
      "stored_procedures": associated_stored_procedures
    }
    obj[db_object_name] = result
    result_list.append(obj)

  return result_list
  

print(run())