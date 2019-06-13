#!/usr/bin/python3

import pandas as pd
import os
import datetime


ID = "42"

############## pattern to check ################
day1 = 0
day2 = 0
day3 = 0
how_many_days_back = 8
###############################################


################ settings dates variables ###############################
today = datetime.date.today()
final_days_set = today - datetime.timedelta(days=how_many_days_back)
yesterday = today - datetime.timedelta(1)
########################################################################


class ReportAbsent:

    def __init__(self, key_api):
        self.key_api = key_api
        self.url = f'https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&Report_StartDate={final_days_set}&Report_EndDate={yesterday}&id={ID}&exportformat=csv'
        self.raw_data = pd.read_csv(self.url)

    def check_for_absent_pattern(self, data):

        ''' this will only will check for the last 3 days if there are absent '''
        for item in range(len(data)-3):
            if data[item] == day1 and data[item + 1] == day2 and data[item + 2] == day3:
                return True
        else:
            return False

    def analyze_data(self):

        filtered_data = self.raw_data.drop(['Employee ID', 'Title', 'Total Hours', 'Hourly Rate', 'Total Pay'], axis=1)
        filtered_data = filtered_data[[x for x in filtered_data.columns if ('Sat' not in x) & ('Sun' not in x)]]
        complete_filter = filtered_data.groupby('Employee').sum()
        complete_filter.to_csv('out_send.csv')
        complete_filter['long_Absent'] = complete_filter.apply(self.check_for_absent_pattern, axis=1)
        final_data = complete_filter[complete_filter['long_Absent']]
        return final_data

    def display_data(self):

        print(self.analyze_data().to_string())



if __name__ == '__main__':

    active = ReportAbsent()
    active.display_data()
