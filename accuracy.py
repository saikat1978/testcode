import pandas as pd
import sys
import os

gr = sys.argv[1]
sheet = sys.argv[2]

CSV_BASE_DIR = '/Users/saikatchatterjee/Documents/SDSM/OneDrive-2021-04-27'
csvFile = os.path.join(CSV_BASE_DIR, sheet + '.csv')

df = pd.read_excel(gr, sheet_name=sheet.strip(), usecols=['SN', 'GT'])
df = df.dropna()
df = df.reset_index(drop=True)
dataDict = df.to_dict(orient='records')
#print(dataDict)

dfCsv = pd.read_csv(csvFile, header=None, usecols=[0, 4])
dfCsv = dfCsv.to_dict(orient='records')

csvMap = {}

for item in dfCsv:
    serial = str(item[0])
    value = item[4]
    csvMap[serial] = value

#print(csvMap)

dataSize = len(dataDict)
correct = 0

for item in dataDict:
    serial = str((item['SN']))
    #print(serial)
    gt = item['GT']
    csvValue = csvMap[serial] if serial in csvMap else 'DB Error'
    #print(serial, gt, csvValue.upper())   
    if gt.strip() == csvValue.strip().upper():
        correct = correct + 1

print(dataSize, correct) 
prcnt = 100.0 * correct / dataSize
print(prcnt)



