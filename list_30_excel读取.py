import openpyxl

wb = openpyxl.load_workbook(r'D:\学习资料\毕业设计\数据\溶血率.xlsx')
print(wb.sheetnames)

# for sheet in wb:
#     print(sheet.title)

# mySheet = wb.create_sheet('mySheet')
# print(wb.sheetnames)

# sheet3 = wb.get_sheet_by_name('Sheet3')
# sheet4 = wb['mySheet']

###Getting cells from the sheets
ws = wb.active
# print(ws)
# print(ws['A1'])
# print(ws['A1'].value)
# print('间隔符')
# c = ws['B1']
# print('Row {}, column {} is {}'.format(c.row, c.column, c.value))
# print('cell {} is {}'.format(c.coordinate, c.value))

# print(ws.cell(row = 1, column = 2))
# print(ws.cell(row = 1, column = 2).value)

# for i in range(1,8,1):
#     print(i, ws.cell(row=i, column = 2).value)

###Getting rows and column from the sheets 
# colC = ws['C']
# print(colC[2].value)
# row6 = ws[6]
# col_range = ws['B:C']
# row_range = ws[2:6]

# for col in col_range:
#     for cell in col:
#         print(cell.value)

# for row in row_range:
#     for cell in row:
#         print(cell.value)

# for row in ws.iter_rows(min_row=1, max_row=2, max_col=2):
#     for cell in row:
#         print(cell)

# print(tuple(ws.rows))

# cell_range = ws['A1:C3']

# for rowofcellobjects in cell_range:
#     for cellobj in rowofcellobjects:
#         print(cellobj.coordinate, cellobj.value)
#     print('---------------End of Row-------------')

print('{} * {}'.format(ws.max_row, ws.max_column))

from openpyxl.utils import get_column_letter, column_index_from_string
print(get_column_letter(2),get_column_letter(47),get_column_letter(900))
print(column_index_from_string('AAH'))