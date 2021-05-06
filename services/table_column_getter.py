import ipdb

class TableColumnGetter:

  def __init__(self, cursor):
    self.cursor = cursor
    self.tables_columns = self.getter()
    
  # Query for all list of table names to call get_column_names on
  def getter(self):
    sql = "select table_name from information_schema.tables"
    self.cursor.execute(sql)
    tables = self.cursor.fetchall()
    tables_columns = []
    for table in tables:
      table_name = table["table_name"]
      column_list = self.get_column_names(table_name=table_name)
      new_obj = {f"{table_name}": f"{column_list}"}
      tables_columns.append(new_obj)

    return tables_columns


  def get_column_names(self, table_name):
    sql = (f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{table_name}';")
    self.cursor.execute(sql)
    columns = self.cursor.fetchall()
    column_list = []
    for column in columns:
      column_name  = column["COLUMN_NAME"]
      column_list.append(column_name)
    
    return column_list

  






