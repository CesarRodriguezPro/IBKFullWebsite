import pandas as pd
import datetime
import os


class ItControl:

    def __init__(self, first_name, last_name, location_request):

        # basic settings for timestation
        self.first_name = first_name
        self.last_name = last_name
        self.location_request = location_request
        self.key_api = os.environ.get('TimeStationKey')

        # get the information for current employees
        self.code_current = 37
        self.url_current = f"https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&id={self.code_current}&exportformat=csv"
        # self.current_data = pd.read_csv(self.url_current)

        self.current_data = pd.read_csv(r"C:\Users\strea\Desktop\testfiles\test_data.csv")
        self.filter_data_in = self.current_data[self.current_data['Status'].str.contains('In')]

    def save_current(self):
        data_pd, location_name = self.current_location()
        return data_pd.to_csv(), location_name
    
    def get_list_of_location(self):
        ''' this return a list of the current locations'''
        raw_data = self.current_data.groupby(['Primary Department']).any()
        data = raw_data.to_dict('index')
        return [location_item for location_item in data.keys()]

    def current_working_locations(self):
        raw_data = self.filter_data_in.groupby(['Current Department']).count()
        return raw_data.to_dict('index')

    def current_location(self):
        '''this function will search for the current location of the user has log in.'''
        if not self.location_request:
            try:
                location = self.foreman_location()
                data_current = self.filter_data_in[(self.filter_data_in['Current Department'].isin([location]))]
                return data_current, location
            except:
                return self.filter_data_in, 'All Locations'

        elif self.location_request == 'allLocations':
            return self.filter_data_in, 'All Locations'

        elif self.location_request:
            data_current = self.filter_data_in[(self.filter_data_in['Current Department'].isin([self.location_request]))]
            return data_current, self.location_request


    def foreman_location(self):
        data = self.current_data[self.current_data['Name'].isin([f'{self.last_name}, {self.first_name}'])]['Primary Department']
        return data.to_list()[0]

    def current_employees_count(self):
        current_location = self.current_location()[0]
        return str(current_location.Name.count())

    def list_of_devices(self):
        data_current = self.current_location()[0] # this will get the data for current location as pandas dataframe.
        devices_view = data_current.groupby(['Device']).count()
        return None if devices_view['Current Department'].empty else devices_view['Current Department'].to_dict()

    def warning_not_today_clock_in(self):
        data_current = self.current_location()[0]
        last_check_in = data_current[data_current['Date'] != datetime.date.today().strftime('%Y-%m-%d')]
        return None if last_check_in.empty else last_check_in.to_dict('index')

    def check_function(self):
        def location_picker():
            if self.current_location()[1] == 'All Locations':
                return self.get_list_of_location()
            else:
                return [self.current_location()[1]]

        location  = location_picker()
        data_current = self.filter_data_in[(self.filter_data_in['Current Department'].isin(location))]
        data_primary = self.filter_data_in[(self.filter_data_in['Primary Department'].isin(location))]
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
    active = ItControl('Pavlo', 'Nalyvayko', None)
    # active.current_data.to_csv('test_data.csv')
    active.save_current()
