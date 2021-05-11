import pandas as pd
import json
import csv
from google.oauth2 import service_account
import pygsheets
import ipdb

with open('service_account.json') as source:
    info = json.load(source)
credentials = service_account.Credentials.from_service_account_info(info)

client = pygsheets.authorize(service_account_file='service_account.json')
ipdb.set_trace()
# class Formatter:

#   def __init__(self, array):
#     self.array = array
#     self.formatted_message = self.format_for_google_sheets()


#   def format_for_google_sheets(self):
#     ipdb.set_trace()
#     # python array of dicts
#     # assign key[i] = row[0], value = row[1]
#     return self.tc

#   def insert_into_gs(self):
#     return self
  






