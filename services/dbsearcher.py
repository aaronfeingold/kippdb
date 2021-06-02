import json

class DbSearcher:

  def __init__(self, dbc):
    self.dbc = dbc
    self.exceptions = self.exceptions()


  # Query dbwh and return an itterable array of all table names
  # will be sorted at main run time
  def list_table_names_from_db(self):
    sql = "SELECT table_name FROM information_schema.tables"
    self.dbc.cursor.execute(sql)
    tables = self.dbc.cursor.fetchall()
    table_names_list = []

    # change slice of tables list here
    # ex-> for table in tables[1:5]: do something
    for table in tables:
      if table["table_name"] not in self.exceptions:
        table_name = table["table_name"]
        table_names_list.append(table_name)

    if table_names_list:
      return table_names_list
    else:
      return "ERROR"


  def find(self, source, targets):
    if targets == "views":
      return self.get_associated_views(source)
    if targets == "triggers":
      return self.get_associated_triggers(source)
    if targets == "stored_procedures":
      return self.get_associated_stored_procedures(source)


  # runs sql on a given table and returns all associated views
  def get_associated_views(self, table_name):
    sql = f"SELECT Name FROM sys.views WHERE OBJECT_DEFINITION(OBJECT_ID) LIKE '%{table_name}%'"
    self.dbc.cursor.execute(sql)
    views = self.dbc.cursor.fetchall()

    formatted_views = []
    for view in views:
      formatted_views.append(view['Name'])

    return formatted_views

  # runs sql on a given table and returns all associated triggers
  def get_associated_triggers(self, table_name):
    sql = f"SELECT Name FROM sys.triggers WHERE OBJECT_DEFINITION(OBJECT_ID) LIKE '%{table_name}%'"
    self.dbc.cursor.execute(sql)
    triggers = self.dbc.cursor.fetchall()

    formatted_triggers = []
    for trigger in triggers:
      formatted_triggers.append(trigger['Name'])

    return formatted_triggers


  # runs sql on a given table and returns all associated stored procedures
  def get_associated_stored_procedures(self, table_name):
    sql = f"SELECT Name FROM sys.procedures WHERE OBJECT_DEFINITION(OBJECT_ID) LIKE '%{table_name}%'"
    self.dbc.cursor.execute(sql)
    procedures = self.dbc.cursor.fetchall()

    formatted_procedures = []
    for procedure in procedures:
      formatted_procedures.append(procedure['Name'])

    return formatted_procedures


  # load in any exceptions, ie known troublemakers for syntax error
  def exceptions(self):
    secrets = json.loads(open("secrets.json").read())
    exceptions = secrets["exceptions"]

    return exceptions



  # getter does the work of packaging up all info
  # returns the ultimate query for what columns are in any table
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

  # runs sql on a given view and returns all associated tables
  def get_tables_associated_to_view(self):
    sql = (f"""SELECT DISTINCT v.name AS view_name, t.name AS table_name
    FROM sys.sql_dependencies d
    INNER JOIN sys.views v ON v.object_id = d.object_id
    INNER JOIN sys.tables t ON t.object_id = d.referenced_major_id
    ORDER BY view_name, table_name""")
    self.dbc.cursor.execute(sql)
    tables = self.dbc.cursor.fetchall()

    return tables

  # runs sql on a given stored procedure and returns all associated tables  
  def get_tables_associated_to_proc(self):
    sql = (f"""SELECT DISTINCT v.name AS proc_name, t.name AS table_name
    FROM sys.sql_dependencies d
    INNER JOIN sys.procedures v ON v.object_id = d.object_id
    INNER JOIN sys.tables t ON t.object_id = d.referenced_major_id
    ORDER BY proc_name, table_name""")
    self.dbc.cursor.execute(sql)
    tables = self.dbc.cursor.fetchall()

    return tables



