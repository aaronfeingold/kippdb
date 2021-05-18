import ipdb
import numpy as np
import json

class DbSearcher:

  def __init__(self, dbc):
    self.dbc = dbc
    self.exceptions = self.exceptions()

  def find(self, source, targets):
    if targets == "views":
      views = self.get_associated_views(source)
      return views
    if targets == "triggers":
      triggers = self.get_associated_triggers(source)
      return triggers
    if targets == "stored_procedures":
      procedures = self.get_associated_stored_procedures(source)
      return procedures


  def get_associated_views(self, table_name):
    sql = f"SELECT Name FROM sys.views WHERE OBJECT_DEFINITION(OBJECT_ID) LIKE '%{table_name}%'"
    self.dbc.cursor.execute(sql)
    views = self.dbc.cursor.fetchall()

    return views


  def get_associated_triggers(self, table_name):
    sql = f"SELECT Name FROM sys.triggers WHERE OBJECT_DEFINITION(OBJECT_ID) LIKE '%{table_name}%'"
    self.dbc.cursor.execute(sql)
    triggers = self.dbc.cursor.fetchall()

    return triggers


  def get_associated_stored_procedures(self, table_name):
    sql = f"SELECT Name FROM sys.procedures WHERE OBJECT_DEFINITION(OBJECT_ID) LIKE '%{table_name}%'"
    self.dbc.cursor.execute(sql)
    procedures = self.dbc.cursor.fetchall()

    return procedures


  # load in any exceptions, ie known troublemakers for syntax error
  def exceptions(self):
    secrets = json.loads(open("secrets.json").read())
    exceptions = secrets["exceptions"]

    return exceptions


  # Query and return an itterable array
  def list_table_names_from_db(self):
    sql = "SELECT table_name FROM information_schema.tables"
    self.dbc.cursor.execute(sql)
    tables = self.dbc.cursor.fetchall()
    table_names_list = []

    for table in tables:
      if table["table_name"] not in self.exceptions:
        table_name = table["table_name"]
        table_names_list.append(table_name)

    if table_names_list:
      return table_names_list
    else:
      return "ERROR"


  # getter does the work of packaging up all info
  # returns the ultimate query
  def tables__columns_getter(self):
    tables_columns = []

    for table_name in self.table_names:
      print(table_name)
      if table_name not in self.exceptions:
        column_list = self.get_column_names(table_name=table_name)
        new_dict = dict()
        new_dict[table_name] = column_list
        tables_columns.append(new_dict)
      else:
        print("ERROR")

    obj = {"tables": tables_columns}
    with open('data.json', 'w') as file:
      json.dump(obj, file)

    return tables_columns


  def get_column_names(self, table_name):
    sql = (f"SELECT column_name FROM information_schema.columns WHERE table_name='{table_name}';")
    self.dbc.cursor.execute(sql)
    columns = self.dbc.cursor.fetchall()
    column_list = []
    for column in columns:
      column_name  = column["column_name"]
      column_list.append(column_name)
    
    return column_list


