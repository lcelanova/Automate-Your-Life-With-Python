import pandas as pd
import openpyxl


file = pd.read_excel('supermarket_sales.xlsx')

print(file[['Gender', 'Product line', 'Total']])

pivote_table = file.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)
print(pivote_table)

pivote_table.to_excel('sales_2021.xlsx', startrow=4, sheet_name='Report')


