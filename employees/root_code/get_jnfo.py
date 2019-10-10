from UniversalRootFolder import TimeStationKey
import datetime
import pandas as pd
from dateutil import relativedelta
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_store = os.path.join(BASE_DIR, 'data_stores')
path_data = os.path.join(data_store, 'raw_data')


class GettingTimeSheet:

    def __init__(self):
        self.url, self.save_data, self.update_time = self.data_selector()
        self.raw_data = pd.read_csv(self.url)
        if self.save_data:
            self.employees_to_data_store()

    def data_selector(self):

        ''' this function check if the file already exit or if the file is older that 3 hours '''

        date = self.week_date()
        KEY = TimeStationKey.get_key()
        CODE = 41  # one weeks summary
        PATH_TO_TIMESTATION = f"https://api.mytimestation.com/v0.1/reports/?api_key={KEY}&Report_StartDate={date}&id={CODE}&exportformat=csv"
        date_now = datetime.datetime.now()

        if os.path.isdir(path_data):
            list_files = os.listdir(path_data)
            for file in list_files:
                if file:
                    file = file.replace('.csv', '')       
                    start_date = datetime.datetime.fromtimestamp(float(file))
                    difference = relativedelta.relativedelta(date_now, start_date)
                    if difference.days > 0 or difference.hours > 2:
                        os.remove(os.path.join(path_data, f'{file}.csv'))
                        return PATH_TO_TIMESTATION, True, date_now
                    return os.path.join(path_data, f'{file}.csv'), False, start_date
                return PATH_TO_TIMESTATION, True, date_now
        return PATH_TO_TIMESTATION, True, date_now

    def week_date(self):
        today = datetime.date.today()
        if today.weekday() == 0:
            this_monday = today - datetime.timedelta(today.weekday())
            last_monday = this_monday - datetime.timedelta(weeks=1)
            return last_monday
        else:
            this_monday = today - datetime.timedelta(today.weekday())
            return this_monday

    def run(self, employee):
        detail_data = self.raw_data[self.raw_data['Employee'].isin([employee])].drop([ 'Unnamed: 0', 'Employee ID', 'Title','Hourly Rate','Total Pay'],axis=1, errors='ignore')
        combine_data = detail_data.groupby(by='Employee').sum()
        detail_data = detail_data.drop('Employee',axis=1)
        return combine_data, detail_data, self.update_time

    def employees_to_data_store(self):

        current_time = datetime.datetime.now().timestamp()
        path_to_file = os.path.join(path_data, f'{current_time}.csv')
        if os.path.isdir(path_data):
            self.raw_data.to_csv(os.path.normpath(path_to_file))
        else:
            os.makedirs(path_data)
            self.raw_data.to_csv(os.path.normpath(path_to_file))


if __name__ == '__main__':
    
    pass
