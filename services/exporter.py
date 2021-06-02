import json
import time
import numpy as geek
from pyasn1.type.univ import Null
import pygsheets
import ipdb

class Exporter:
    def __init__(self):
        self.data = self.load_data()
        self.sheet_id = self.get_id()
        self.client = pygsheets.authorize(service_account_file='service_account.json')


    def load_data(self):
        data = json.loads(open("data.json").read())
        
        return data        


    def get_id(self):
        secrets = json.loads(open("secrets.json").read())
        sheet_id = secrets["sheet_id"]

        return sheet_id

    # FYI: 
    # This version of the Google Sheets API has a limit of 500 requests per 100 seconds per project,
    # and 100 requests per 100 seconds per user. Limits for reads and writes are tracked separately.
    # There is no daily usage limit.
    def to_google_sheets(self):
        # conditions for rate exceed
        n = 64
        conditions = []
        a = geek.arange(100)
        for x in a:
            conditions.append(n*x)

        initial_ts = time.time()
        print(initial_ts)
        new_ts = Null

        # make the client connection, anmd select sheet to export to
        spreadsheet = pygsheets.Spreadsheet(client=self.client, id=self.sheet_id)
        worksheet = spreadsheet.worksheet_by_title('NEW_WORKSHEET')
        # two initial requests, followed up with 2 requests per object(array) from data
        number_requests = 2

        for index, array in enumerate(self.data):
            new_ts = time.time()
            elapsed_time = new_ts - initial_ts
            row = index + 1
            view_name_addr = f'A{row}'
            table_name_addr = f'B{row}'

            view_name = array[0]
            table_name = array[1]

            number_requests += 2
            print(number_requests)

            if (number_requests in conditions):
                # sleep until 101s ( be certain we dont have more than 100req in 100)
                print("")
                print(elapsed_time)
                time.sleep(101-elapsed_time)
                print("recommencing")
                initial_ts = time.time()
                print(initial_ts)
                worksheet.update_value(view_name_addr, view_name, parse=None)
                worksheet.update_value(table_name_addr, table_name, parse=None)
            else:
                worksheet.update_value(view_name_addr, view_name, parse=None)
                worksheet.update_value(table_name_addr, table_name, parse=None)
        return "COMPLETE"


 
