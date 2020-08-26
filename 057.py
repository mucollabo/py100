import openpyxl
import os

cwd = os.getcwd()
filename = 'df.xlsx'
filepath = os.path.join(cwd, 'output', filename)

wb = openpyxl.load_workbook(filepath)
print(wb)
print(type(wb))
print(wb.sheetnames)

ws = wb['Sheet1']
print(ws)
print(ws.title)

active_sheet = wb.active
print(active_sheet)