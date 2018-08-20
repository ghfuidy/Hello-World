import openpyxl, pprint

print('Opening the workbook')
wb = openpyxl.load_workbook('storage/censuspopdata.xlsx')
sheet = wb.active

countryData = {}

for row in range(2, sheet.max_row+1):
    #Each row in the spreasheet has data
    state = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)]. value

    countryData.setdefault(state, {})
    countryData[state].setdefault(country,{'tracts': 0, 'pop': 0})
    countryData[state][country]['tracts'] += 1
    countryData[state][country]['pop'] += int(pop)

print('Writing results...')
resultFile = open('census2010.py','w')
resultFile.write('allData = ' + pprint.pformat(countryData))
resultFile.close()