import pandas as pd
import datetime
import os


class ItControl:

    def __init__(self, first_name, last_name):

        # basic settings for timestation
        self.first_name = first_name
        self.last_name = last_name
        self.key_api = os.environ.get('TimeStationKey')

        # get the information for current employees
        # self.code_current = 37
        # self.url_current = f"https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&id={self.code_current}&exportformat=csv"
        # self.current_data = pd.read_csv(self.url_current)

        self.current_data = pd.read_csv(r"C:\Users\strea\Desktop\testdata.csv")
        self.filter_data_in = self.current_data[self.current_data['Status'].str.contains('In')]
    
    def get_list_of_location(self):
        raw_data = self.current_data.groupby(['Primary Department']).any()
        data = raw_data.to_dict('index')
        return [location_item for location_item in data.keys()]

    def current_location(self):
        location = self.foreman_location()
        data_current = self.filter_data_in[(self.filter_data_in['Current Department'].isin([location]))]
        return data_current

    def foreman_location(self):
        data = self.current_data[self.current_data['Name'].isin([f'{self.last_name}, {self.first_name}'])]['Primary Department']
        return data.to_list()[0]

    def current_employees_count(self):
        current_location = self.current_location()
        return str(current_location.Name.count())

    def list_of_devices(self):
        data_current = self.current_location()
        devices_view = data_current.groupby(['Device']).count()
        return None if devices_view['Current Department'].empty else devices_view['Current Department'].to_dict()

    def warning_not_today_clock_in(self):
        data_current = self.current_location()
        last_check_in = data_current[data_current['Date'] != datetime.date.today().strftime('%Y-%m-%d')]
        return None if last_check_in.empty else last_check_in.to_dict('index')

    def check_function(self):
        location  = self.foreman_location()
        data_current = self.filter_data_in[(self.filter_data_in['Current Department'].isin([location]))]
        data_primary = self.filter_data_in[(self.filter_data_in['Primary Department'].isin([location]))]
        primary_no_current = data_current[data_current['Primary Department'] != data_current['Current Department']]
        current_not_primary = data_primary[data_primary['Primary Department'] != data_primary['Current Department']]
        current_not = self.adact_data(current_not_primary)
        primary_not = self.adact_data(primary_no_current)
        return current_not, primary_not

    def adact_data(self, data):
        if not data.empty:
            raw_data = data.sort_values(['Current Department', 'Name']).to_dict('index')
            return self.convert_name(raw_data)
        else:
            return None

    def convert_name(self, dict_in):
        return_list = []
        for item in dict_in.values():
            item['Primary_Department'] = item.pop('Primary Department')
            item['Current_Department'] = item.pop('Current Department')
            return_list.append(item)
        return return_list


if __name__ == '__main__':
    active = ItControl('Pavlo', 'Nalyvayko')
    x = active.get_list_of_location()
    print(x)

