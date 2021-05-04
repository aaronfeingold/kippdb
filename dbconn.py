import pymssql
import json
import sys

secrets = json.loads(open("secrets.json").read())

server = secrets["server"]
user = secrets["user"]
password = secrets["password"]
db = secrets["dbname"]

conn = pymssql.connect(server, user, password, db)
cursor = conn.cursor(as_dict=True)

cursor.execute("Select [NAME] from sysobjects where type = 'P' and category = 0")
# Read and print tables
print(cursor.fetchall())
    


