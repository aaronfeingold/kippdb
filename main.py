import pymssql
import json
import sys
import ipdb
from services.dbconn import GetCursor
from services.table_column_getter import TableColumnGetter

def run():
  cursor = GetCursor.get_cursor()
  tcg = TableColumnGetter(cursor=cursor)
  tc = tcg.tables_columns
  
  return tc


print(run())