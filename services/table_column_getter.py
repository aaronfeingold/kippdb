import ipdb
import json

class TableColumnGetter:

  def __init__(self, cursor):
    self.cursor = cursor
    self.exceptions = self.exceptions()
    self.table_names = self.get_table_names_from_db()
    self.tables_columns = self.getter()
  
  
  def exceptions(self):
    secrets = json.loads(open("secrets.json").read())
    exceptions = secrets["exceptions"]

    return exceptions


  # Query and iterate for all array of table names to call get_column_names on
  def get_table_names_from_db(self):
    sql = "SELECT table_name FROM information_schema.tables"
    self.cursor.execute(sql)
    tables = self.cursor.fetchall()
    table_names = []
    for table in tables:
      table_name = table["table_name"]
      table_names.append(table_name)

    if table_names:
      return table_names
    else:
      return "ERROR"
    
    ipdb.set_trace()


  def getter(self):
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

    return tables_columns


  def list_all_table_names(tables):
    ipdb.set_trace()
    tables_list = []
    for table in tables:
      table_name = table["table_name"]
      tables_list.append(table_name)

    return tables_list


  def get_column_names(self, table_name):
    sql = (f"SELECT column_name FROM information_schema.columns WHERE table_name='{table_name}';")
    self.cursor.execute(sql)
    columns = self.cursor.fetchall()
    column_list = []
    for column in columns:
      column_name  = column["column_name"]
      column_list.append(column_name)
    
    return column_list


