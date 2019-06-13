import pandas as pd
import datetime
import os
        


class IrregularEntries:

    def __init__(self,key_api):
     
        self.key_api = os.environ.get('TimeStationKey')
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
        ' working in this part to adact this funtion to html views.'
        sorted_db = self.process_information()
        
        print('')


    def display_data(self):
        sorted_db = self.process_information()
        if not sorted_db.empty:
            print('This are Irregular entries -> please check \n ')
            print(sorted_db[sorted_db['flag']][['Name', 'Department', 'Date','Time', 'Activity']].to_string())
            print(self.brk)

if __name__ == "__main__":
    pass