import pandas as pd
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference
import string


file = pd.read_excel('supermarket_sales.xlsx')

pivote_table = file.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)

pivote_table.to_excel('sales_2021.xlsx', startrow=4, sheet_name='Report')

workbook = load_workbook('sales_2021.xlsx')

tab = workbook['Report']

min_column = workbook.active.min_column
max_column = workbook.active.max_column
min_row = workbook.active.min_row
max_row = workbook.active.max_row

#plotting

barchart = BarChart()

data = Reference(tab, min_col=min_column+1, max_col=max_column, min_row=min_row, max_row=max_row)
categories = Reference(tab, min_col=min_column, max_col=min_column, min_row=min_row+1, max_row=max_row)

barchart.add_data(data, titles_from_data=True)
barchart.set_categories(categories)
barchart.style = 2
barchart.title = 'Ventas'

tab.add_chart(barchart, 'B12')
tab['A8'] = 'SUMA'

tab['B8'] = '=SUM(B6:B7)'
tab['B8'].style = 'Currency'

abc = list(string.ascii_uppercase)
abc[]
print(abc)

workbook.save('sales_2021.xlsx')

