
import pandas as pd
import datetime

today = datetime.date.today()
last_monday = today - datetime.timedelta(6)
#last_monday = today - datetime.timedelta(days=today.weekday())
date= last_monday.strftime('%Y-%m-%d')

class HoursGreater:

    def __init__(self, key_api, brk):
        self.brk = brk
        self.key_api = key_api
        self.CODE = 41
        self.url = f"https://api.mytimestation.com/v0.1/reports/?api_key={self.key_api}&Report_StartDate={date}&id={self.CODE}&exportformat=csv"
        self.df = pd.read_csv(self.url)

    def hours_greater(self, location):

        ''' This will display in the main view if employees has hours greater that 15,
        if employees forgot to clock out the previous days this report will help to see those employees
        '''

        filter_data = self.df[self.df['Department'].str.contains(location)]
        col = filter_data.iloc[:, 4:-3].columns.values
        lb = list(col)
        lb.insert(0, 'Employee')
        lb.insert(1, 'Department')
        
        #  i need to make global so i can be print from the outsite of this functions.
        global great_hours
        great_hours = filter_data[filter_data[filter_data[col] > 15][col].notnull().any(1)][lb]
        
        if great_hours.empty:
            pass
        else:
            print('\n\nWarning ----> Please review Employees hours on timestation')
            print(self.brk)            
            print(great_hours.to_string())
            print(self.brk)            
            print('\n')