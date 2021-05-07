import pymssql
import json
import sys
from services.dbconn import DBConnector
from services.table_column_getter import TableColumnGetter
import ipdb

def run():
  dbc = DBConnector()
  cursor = dbc.cursor
  tcg = TableColumnGetter(cursor=cursor)
  tc = tcg.tables_columns
  
  return tc


print(run())