import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side

class vacationRequestBuilder:

    def __init__(self, employee, date_in, date_out, foreman):
        self.employee = employee
        self.date_in = date_in
        self.date_out = date_out
        self.foreman = foreman



    def run(self):

        wb = openpyxl.Workbook()
        ws = wb.active

        


        wb.save()
        wb.close()