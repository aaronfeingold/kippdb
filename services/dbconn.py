import pymssql
import json
import ipdb

class GetDatabaseConnection:

  def __init__(self):
    self.conn = self.conn()
    self.cursor = self.get_cursor()

  def conn(self):
    secrets = json.loads(open("secrets.json").read())

    server = secrets["servers"]["server1"]
    user = secrets["users"]["user1"]["username"]
    password = secrets["users"]["user1"]["password"]
    db = secrets["dbname"]

    conn = pymssql.connect(server, user, password, db)

    return conn

  def get_cursor(self):
    cursor = self.conn.cursor(as_dict=True)

    return cursor


