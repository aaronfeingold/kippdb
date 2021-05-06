import pymssql
import json

class GetCursor:

  def get_cursor():
    secrets = json.loads(open("secrets.json").read())

    server = secrets["server"]
    user = secrets["user"]
    password = secrets["password"]
    db = secrets["dbname"]

    conn = pymssql.connect(server, user, password, db)
    cursor = conn.cursor(as_dict=True)

    return cursor
