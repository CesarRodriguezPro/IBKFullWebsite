import pandas as pd
import numpy as np
import datetime
from . import TimeStationKey
import os

''' this will check if there is any wrong entry in the timestation entry log '''


class IrregularEntries:
    ''' this will catch wrong entries due synchronization problems '''
    def __init__(self):
        self.key_api = TimeStationKey.get_key()
        self.CODE = 34  # Employee Activity
        self.today = datetime.date.today()
        self.current_monday = self.today - datetime.timedelta(days=self.today.weekday())

        self.url_data = f"https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&" \
            f"Report_StartDate={self.current_monday}&Report_EndDate={self.today}&id={self.CODE}&exportformat=csv"
        self.raw_data = pd.read_csv(self.url_data)

    def process_information(self):
        sorted_db = self.raw_data.sort_values(['Name', 'Date'])
        comparison = sorted_db.shift(-1) == sorted_db
        sorted_db['flag'] = comparison['Name'] & comparison['Date'] & comparison['Activity']
        return sorted_db[sorted_db['flag']]

    def send_to_website(self):
        sorted_db = self.process_information()
        return sorted_db.to_dict('index')


class DailyForemanInfo:
    ''' sometimes the foreman don't clock people in after lunch but clock them in and out by the
    end of the day. this class will catch any entry with less than 10 min different '''

    def __init__(self):
        # settings ---------------------------------------------------------------------------
        self.max_time = 10
        self.key_api = TimeStationKey.get_key()
        self.CODE = 34  # Employee Activity
        self.today = datetime.date.today()
        self.four_days_ago = self.today - datetime.timedelta(days=4) 
        self.yesterday = self.today - datetime.timedelta(days=1)

        self.url_data = f"https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&" \
                        f"Report_StartDate={self.four_days_ago}&Report_EndDate={self.yesterday}&id={self.CODE}&exportformat=csv"
        self.raw_data = pd.read_csv(self.url_data)

    def process_info(self):

        # filter data and organized --------------------------------------------------------------
        self.raw_data['in'] = self.raw_data[self.raw_data['Activity'].str.contains('In')]['Time']
        self.raw_data['pre_out'] = self.raw_data[self.raw_data['Activity'].str.contains('Out')]['Time']
        sorted_data = self.raw_data.sort_values(['Date', 'Name'])
        sorted_data['out'] = sorted_data.shift(-1)['Time']
        filtered_data = sorted_data[sorted_data['pre_out'].isnull()]

        # this convert to datetime objects --------------------------------------------------------
        filtered_data['in'] = pd.to_datetime(filtered_data['Date'] + ' ' + filtered_data['in'])
        filtered_data['out'] = pd.to_datetime(filtered_data['Date'] + ' ' + filtered_data['out'])

        # get the difference between the times in and out   ---------------------------------------
        filtered_data['total'] = (filtered_data['out'] - filtered_data['in'])
        filtered_data['total'] = filtered_data['total'] // np.timedelta64(1, 'm')
        return filtered_data

    def get_short_hours(self, location):
        data = self.process_info()
        print(f'---------->>>> {location}')
        if location != 'All Locations':
            data = data[data['Department'].isin([location])]
        data = data[data['total'] < self.max_time]
        return data.to_dict('index')


if __name__ == "__main__":
    x = TooShortEntries()

