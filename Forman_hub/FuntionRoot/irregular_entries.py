import pandas as pd
import datetime
import os

''' this will check if there is any wrong entry in the timestation entry log '''

class IrregularEntries:

    def __init__(self):
        self.key_api = os.environ.get('TimeStationKey')
        self.CODE = 34  # Employee Activity
        self.today = datetime.date.today()
        self.current_monday = self.today - datetime.timedelta(days=self.today.weekday())

        self.url_data = f"https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&" \
            f"Report_StartDate={self.current_monday}&Report_EndDate={self.today}&id={self.CODE}&exportformat=csv"
        # self.raw_data = pd.read_csv(self.url_data)
        self.raw_data = pd.read_csv(r"C:\Users\strea\Desktop\testfiles\EmployeeActivity.csv")

    def process_information(self):
        sorted_db = self.raw_data.sort_values(['Name', 'Date'])
        comparison = sorted_db.shift(-1) == sorted_db
        sorted_db['flag'] = comparison['Name'] & comparison['Date'] & comparison['Activity']
        return sorted_db[sorted_db['flag']]

    def send_to_website(self):
        sorted_db = self.process_information()
        return sorted_db.to_dict('index')


if __name__ == "__main__":
    active = IrregularEntries()
    active.raw_data.to_csv('EmployeeActivity.csv')
