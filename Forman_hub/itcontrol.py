import pandas as pd
import datetime
import os


class ItControl:

    def __init__(self, location):

        # basic settings for timestation
        self.key_api = os.environ.get('TimeStationKey')
        self.location = location

        # get the information for current employees
        self.code_current = 37
        self.url_current = f"https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&id={self.code_current}&exportformat=csv"
        self.current_data = pd.read_csv(self.url_current)
        self.filter_data_in = self.current_data[self.current_data['Status'].str.contains('In')]
        self.data_current = self.filter_data_in[(self.filter_data_in['Current Department'].str.contains(self.location))]

    def current_employees_count(self):
        return str(self.data_current.Name.count())

    def list_of_devices(self):
        devices_view = self.data_current.groupby(['Device']).count()
        return None if devices_view['Current Department'].empty else devices_view['Current Department'].to_dict()

    def warning_not_today_clock_in(self):
        last_check_in = self.data_current[self.data_current['Date'] != datetime.date.today().strftime('%Y-%m-%d')]
        return None if last_check_in.empty else last_check_in.to_dict()

    def check_function(self):

        data_current = self.filter_data_in[(self.filter_data_in['Current Department'].str.contains(self.location))]
        data_primary = self.filter_data_in[(self.filter_data_in['Primary Department'].str.contains(self.location))]

        primary_no_current = data_current[data_current['Primary Department'] != data_current['Current Department']]
        current_not_primary = data_primary[data_primary['Primary Department'] != data_primary['Current Department']]

        if not current_not_primary.empty:
            current_not = current_not_primary.sort_values(['Current Department', 'Name']).to_dict()
        else:
            current_not = None

        if not primary_no_current.empty:
            primary_not = primary_no_current.sort_values(['Device', 'Name']).to_dict()
        else:
            primary_not = None

        return current_not, primary_not


if __name__ == '__main__':

    active = ItControl('')