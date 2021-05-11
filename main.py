from services.dbconn import DBConnector
from services.table_column_getter import TableColumnGetter
# from services.formatter import Formatter
# from services.exporter import GoogleSheetsExporter
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
  # send array of key-value pairs to the formatter
  # return them for the exporter
  # then use formatted text to insert into google sheets doc.
  
  return tc

print(run())