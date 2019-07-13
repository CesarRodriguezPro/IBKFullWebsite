import pandas as pd
import datetime
from . import TimeStationKey

today       = datetime.date.today()
this_monday = today - datetime.timedelta(days=(today.weekday()))
last_monday = this_monday - datetime.timedelta(weeks=1)
yesterday   = today - datetime.timedelta(days=1)
key         = TimeStationKey.get_key()


class PreviousWeekTimeSheet:
    def __init__(self, location):
        self.key_api = key
        self.location = location
        self.CODE = 41  # 1 week summary
        self.url = f"https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&Report_StartDate={last_monday}&id={self.CODE}&exportformat=csv"
        self.raw_data = pd.read_csv(self.url)

    def run(self):
        data_clean = self.raw_data.drop(['Employee ID', 'Title', 'Hourly Rate', 'Total Pay'], axis=1)
        filter_data = data_clean[data_clean['Department'].isin([self.location])]
        return filter_data.to_dict('index')


class CurrentWeekTimeSheet:
    def __init__(self, location):
        self.key_api = key
        self.location = location
        self.CODE = 42  # detail summary
        self.url = f"https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&Report_StartDate={this_monday}&Report_EndDate={yesterday}&id={self.CODE}&exportformat=csv"
        self.raw_data = pd.read_csv(self.url)

    def run(self):
        data_clean = self.raw_data.drop(['Employee ID', 'Title', 'Hourly Rate', 'Total Pay'], axis=1)
        filter_data = data_clean[data_clean['Department'].isin([self.location])]
        return filter_data.to_dict('index')

