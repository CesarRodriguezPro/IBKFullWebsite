import os, datetime
import pandas as pd
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
from UniversalRootFolder import TimeStationKey


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
osha_path = os.path.join(BASE_DIR, 'osha_file', 'osha30.xlsx')

######################## settings #########################################################################
API_KEY = TimeStationKey.get_key()
CODE = 37 # current Status
URL = 'https://api.mytimestation.com/v0.1/reports/?api_key={}&id={}&exportformat=csv'.format(API_KEY, CODE)
###########################################################################################################

list_topics = [
    "SAFETY DISCUSSION (REVIEW ACTIVITIES/TASK TO BE PERFORMED INCLUDING SAFETY CONCERNS OR RISK WITH WORK)",
    '[ ] Fall Protection:',
    '',
    '[ ] Control Access Zone:',
    '',
    '[ ] Proper use of pneumatic tools',
    '',
    '[ ] Safety of Handset Forms installation.',
    '',
    '[ ] Safety of Plywood installation.',
    '',
    '[ ] Ergonomics',
    '',
    '[ ] hazardous Materials',
    '',
    '[ ] OSHA Silica Standard',
    '',
    '[ ] Use of Proper PPE:',
    '',
    '[ ] Proper use of Electrical Tools',
    '',
    '[ ] Safety of TITAN Installation.',
    '',
    '[ ] Safety of Rebar installation.',
    '',
    '[ ] Safety of Hosting and Lifting.',
    '',
    '[ ] Unusual Weather Conditions.',
    '',
    '[ ] Safety of Concrete Pour',
    '',
    '[ ] Stripping Operations',
    '',
    '',
    '',
]


class CheckOsha:
    ''' this read a excel file with the names and the dates in which the osha 30 hours expire 
    and compare with the names that are working at this moment '''

    def __init__(self):
        self.raw_data = pd.read_excel(osha_path)
        self.DB_data = self.raw_data[~self.raw_data['OSHA-30exp'].isna()]

    def check_employee(self, name):
        info = self.DB_data[self.DB_data['Employee name'].str.contains(name)]['OSHA-30exp']
        if info.empty:
            return ''
        else:
            for date in info.to_dict().values():
                return date.strftime("%Y-%m-%d")

    def display_info(self):
        print(self.DB_data.head())


class TimeStationInfo:

    def __init__(self):

        self.URL = URL
        self.raw_current = pd.read_csv(self.URL)
        self.osha = CheckOsha()
        self.current_in = self.raw_current[self.raw_current['Status'].str.contains('In')]
        self.current_in['osha'] = self.current_in['Name'].apply(self.osha.check_employee)
    
    def list_devices(self, location):
        by_location = self.current_in[self.current_in['Current Department'].isin([location])]
        devices = by_location.groupby(['Device']).all()
        unpack = [ x for x in devices.to_dict('index').keys()]
        return unpack

    def run(self, location, device):
        ''' this return pandas dataframe filter by location '''
        filter_data = self.current_in[self.current_in['Current Department'].isin([location])]
        filter_by_device = filter_data[filter_data['Device'].isin([device])]
        total_employees = filter_by_device['Name'].count()
        employees = filter_by_device[['Name', 'osha']]
        employees_dict = employees.to_dict('index')
        return employees_dict, total_employees

    def save_time_sheet(self):
        self.current_in.to_csv('testCurrent.csv')


if __name__ == "__main__":
    pass


