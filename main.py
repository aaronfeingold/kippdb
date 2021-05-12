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
      # export = Exporter(tc=tc)
  ## PROBLEM:
    ## cannot export while VPN is connected
    ## have attempted to write bash, expect, and python file to deal with Cisco VPN
    ## did no get that working yet
    ## current work around is to run main, then manually shut down VPN
    ## then, run the exporter
      # msg = export.to_google_sheets()
      # return msg
  
  

print(run())