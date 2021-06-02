from services.dbconn import GetDatabaseConnection
from services.dbsearcher import DbSearcher
import csv

def run():
  print("connecting")
  dbc = GetDatabaseConnection()
  print("connected...searching")
  dbs = DbSearcher(dbc)

  # length of list can be adjust Dbsearcher
  print("querying db for list of tables")
  tables_list = dbs.list_table_names_from_db()

  print("querying db for associations to tables")
  result_list = []

  # this is a lot of code for a main. this can be abstracted to another service
  # could be called "db_obj_maker" and called on each obj
  # each obj then get exported?
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
  
  # for now, we will export to CSV and then copy and paste over to google sheets
  # this seems obviously redundant, why not just go straight to csv?
  # reason: not convinced this should be written to a file here, but rather is 
  # exported (by an export module) to a more user friendly source.
  # however, vpn makes it impossible to use GoogleSheets at api
  # and the script to toggle vpn on and off is more complex than necessary for the
  # purposes of the dbwh dictionary.

  with open('map.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for row in result_list:
      res = list(row.keys())
      table_name = str(res[0])
      views = row[table_name]["views"]
      triggers = row[table_name]["triggers"]
      stored_procedures = row[table_name]["stored_procedures"]
      t = (table_name, views, triggers, stored_procedures)
      writer.writerow(t)
  
  return "COMPLETE"

print(run())