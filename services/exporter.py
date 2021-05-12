import pandas as pd
import json
import csv
from google.oauth2 import service_account
import pygsheets
import ipdb


class Exporter:
    def __init__(self):
        self.tc = self.load_tc()
        self.sheet_id = self.get_id()
        self.client = pygsheets.authorize(service_account_file='service_account.json')

    def load_tc(self):
        data = json.loads(open("data.json").read())
        tc = data["tables"]

        return tc        


    def get_id(self):
        secrets = json.loads(open("secrets.json").read())
        sheet_id = secrets["sheet_id"]

        return sheet_id


    def to_google_sheets(self):
        spreadsheet = pygsheets.Spreadsheet(client=self.client, id=self.sheet_id)
        worksheet = spreadsheet.worksheet_by_title('NEW_WORKSHEET')

        for index, table in enumerate(self.tc):
            row = index + 1
            table_name_addr = f'A{row}'
            column_list_addr = f'B{row}'

            tb_val = ""
            for key in table.keys():
                tb_val = key
            
            cl_val = ', '.join(table[tb_val])

            worksheet.update_value(table_name_addr, tb_val, parse=None)
            worksheet.update_value(column_list_addr, cl_val, parse=None)
        
        return "COMPLETE"
        


export = Exporter()
msg = export.to_google_sheets()

print(msg)
  