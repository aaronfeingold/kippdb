import pymssql
import json
import ipdb

class DBConnector:

  def __init__(self):
    self.conn = self.conn()
    self.cursor = self.get_cursor()

  def conn(self):
    secrets = json.loads(open("secrets.json").read())

    server = secrets["server"]
    user = secrets["user"]
    password = secrets["password"]
    db = secrets["dbname"]

    conn = pymssql.connect(server, user, password, db)

    return conn

  def get_cursor(self):
    cursor = self.conn.cursor(as_dict=True)

    return cursor


