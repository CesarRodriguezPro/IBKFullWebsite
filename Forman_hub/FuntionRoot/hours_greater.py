
import pandas as pd
import datetime
import os

today = datetime.date.today()
past_date = today - datetime.timedelta(6)
date= past_date.strftime('%Y-%m-%d')

class HoursGreater:

    def __init__(self):

        self.key_api = os.environ.get('TimeStationKey')
        self.CODE = 41 # 1 week summary
        self.url = f"https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&Report_StartDate={date}&id={self.CODE}&exportformat=csv"
        self.raw_data = pd.read_csv(self.url)
        # self.raw_data = pd.read_csv(r"C:\Users\strea\Desktop\testfiles\1weekSummary.csv")

    def get_times(self):
        data = self.raw_data
        just_columns = data.iloc[:, 5:-3].columns.values
        lb = list(just_columns)
        lb.insert(0, 'Employee')
        lb.insert(1, 'Department')
        great_hours = data[data[data[just_columns] > 15 ][just_columns].notnull().any(1)][lb]
        return great_hours.to_dict('split')

if __name__ == "__main__":
    active = HoursGreater()
    data = active.get_times()
    active.raw_data.to_csv('1weekSummary.csv')
