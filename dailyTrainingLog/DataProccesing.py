import pandas as pd
from UniversalRootFolder import TimeStationKey
import os, datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
osha_path = os.path.join(BASE_DIR, 'media','data.xlsx')

######################## settings #########################################################################
API_KEY = TimeStationKey.get_key()
CODE = 37 # current Status
URL = 'https://api.mytimestation.com/v0.1/reports/?api_key={}&id={}&exportformat=csv'.format(API_KEY, CODE)
###########################################################################################################


class GetDataFromTimeStation:
    def __init__(self, location):

        self.location = location
        self.raw_current = pd.read_csv(URL)
        self.current_in = self.raw_current[self.raw_current['Status'].str.contains('In')]
        self.current_location = self.current_in[self.current_in['Current Department'].isin([location])]
        self.database = pd.read_excel(osha_path)

    def conver_time(self, date):
        try:
            formated_date = date.strftime('%m/%d%/%Y')
            return formated_date
        except:
            return None

    def run(self):
        data = self.database['Employee name'].isin(self.current_location['Name'])
        selected_data = self.database[data][['Employee name', 'TITLE','OSHA-30No', 'OSHA-30exp']]
        selected_data['Name'] = selected_data['Employee name']
        selected_data['OSHANumber'] = selected_data['OSHA-30No']
        selected_data['OSHAExp'] = selected_data['OSHA-30exp'].apply(self.conver_time)


        not_in_db = self.current_location['Name'].isin(self.database['Employee name'])
        no_in = self.current_location[~not_in_db]
        return selected_data.to_dict('index'), no_in.to_dict('index')

