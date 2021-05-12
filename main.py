from services.dbconn import DBConnector
from services.table_column_getter import TableColumnGetter
from services.exporter import Exporter
import ipdb

def run():
  # use pymssql to connect to a db
  dbc = DBConnector()
  # set a variable to the returned object of dbc cursor
  cursor = dbc.cursor
  # use that cursor to query db
  tcg = TableColumnGetter(cursor=cursor)
  # returns an array containing a dict for every table
  # for each, key is tablename, value is an array of 
  # strings representing the column_names for that table.
  tc = tcg.tables_columns
  ## TO-DO: 
  # send array of key-value pairs to the exporter
  export = Exporter(tc=tc)
  msg = export.to_google_sheets
  
  return tc

print(run())