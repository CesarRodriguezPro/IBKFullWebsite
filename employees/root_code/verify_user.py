import pandas as pd
from UniversalRootFolder import TimeStationKey
import os
import datetime
from dateutil import relativedelta

''' these function will verify if the employees is in Timestation 
i will donwload a CSV file from the API and compare the name giving in the employees/home.html
also will return the name as its properly time in timestation.
also will check if the data download it from the API is older than 4 hours if it is will renew it.'''

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_store = os.path.join(BASE_DIR, 'data_stores')
path_list_employees = os.path.join(BASE_DIR, 'data_stores', 'list_employees')
KEY = TimeStationKey.get_key()
PATH_TO_TIMESTATION = f"https://api.mytimestation.com/v0.1/reports/?api_key={KEY}&id=35&exportformat=csv"


class Verify:

    def __init__(self):
        ''' here the self.data_selector will return the correct url for pandas and also
        a True or False value in the self.save_data '''

        self.url, self.save_data = self.data_selector()
        self.raw_data = pd.read_csv(self.url)
        if self.save_data:
            self.employees_to_data_store()


    def data_selector(self):

        ''' this will return the main source of information and the order to save the csv to local.
        if the csv download it is older than 4 hours will erase the file and download a new one
        this will prevent unnecessary use of the time-station server '''

        if os.path.isdir(path_list_employees):
            list_files = os.listdir(path_list_employees)
            for file in list_files:
                if file:
                    file = file.replace('.csv', '')
                    start_date = datetime.datetime.fromtimestamp(float(file))
                    end_date = datetime.datetime.now()
                    difference = relativedelta.relativedelta(end_date, start_date)

                    if difference.days > 0 or difference.hours > 12:
                        os.remove(os.path.join(data_store, 'list_employees', f'{file}.csv'))
                        return PATH_TO_TIMESTATION, True
                    return os.path.join(path_list_employees, f'{file}.csv'), False
                return PATH_TO_TIMESTATION, True
        return PATH_TO_TIMESTATION, True

    def verify(self, last_name, card_number):
        data = self.raw_data[self.raw_data['Card Number'].isin([card_number])]
        list_data = data.to_dict('index')
        for items in list_data.values():
            if last_name.lower() in items['Name'].lower():
                return items['Name']
            else:
                return None

    def employees_to_data_store(self):
        current_time = datetime.datetime.now().timestamp()
        path_to_file = os.path.join(path_list_employees, f'{current_time}.csv')
        if os.path.isdir(path_list_employees):
            self.raw_data.to_csv(os.path.normpath(path_to_file))
        else:
            os.makedirs(path_list_employees)
            self.raw_data.to_csv(os.path.normpath(path_to_file))


if __name__ == '__main__':
    x = Verify()
    print(x.data_selector())