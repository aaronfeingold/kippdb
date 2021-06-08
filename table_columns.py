from services.dbconn import GetDatabaseConnection
from services.dbsearcher import DbSearcher

def run():
  print("connecting")
  dbc = GetDatabaseConnection()
  print("connected...searching")
  dbs = DbSearcher(dbc)
  # length of list can be adjusted in Dbsearcher
  print("querying db for list of tables")
  tc = dbs.tables__columns_getter()

  return tc

run()
