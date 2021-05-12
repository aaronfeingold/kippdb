import pandas as pd
import json
import csv
from google.oauth2 import service_account
import pygsheets
import ipdb

client = pygsheets.authorize(service_account_file='service_account.json')
url = "https://docs.google.com/spreadsheets/d/1A5M7Qyfjj-XTm6q_9A3xT_dv4pfutU0bRs6OxjiMax8/edit?usp=sharing"
sheet_id = "1A5M7Qyfjj-XTm6q_9A3xT_dv4pfutU0bRs6OxjiMax8"
spreadsheet = pygsheets.Spreadsheet(client=client, id=sheet_id)
worksheet = spreadsheet.worksheet_by_title('NEW_WORKSHEET')
addr = "A1"
val = "HELLO WORLD"
worksheet.update_value(addr, val, parse=None)
ipdb.set_trace()




