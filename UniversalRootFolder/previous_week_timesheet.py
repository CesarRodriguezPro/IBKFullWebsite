import pandas as pd
import datetime
import os

today = datetime.date.today()
last_monday = today - datetime.timedelta(days=today.weekday())


class PreviousWeekTimeSheet:
    def __init__(self, location):
        self.key_api = os.environ.get('TimeStationKey')
        self.location = location
        self.CODE = 41  # 1 week summary
        self.url = f"https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&Report_StartDate={last_monday}&id={self.CODE}&exportformat=csv"
        self.raw_data = pd.read_csv(self.url)

    def run(self):
        data_clean = self.raw_data.drop(['Employee ID', 'Title', 'Hourly Rate', 'Total Pay'], axis=1)
        filter_data = data_clean[data_clean['Department'].isin([self.location])]
        return filter_data.to_dict('index')

if __name__ == '__main__':

    active = PreviousWeekTimeSheet(location='161E 28ST (SS)')
    data = active.run()
    x = [x.keys() for x in data.values()][0]
    print(list(x)[2:-1])