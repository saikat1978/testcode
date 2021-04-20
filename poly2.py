import pandas as pd
import sys
import os
import math
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
import seaborn as sns


csvFile = sys.argv[1]

df = pd.read_csv(csvFile, header=[0, 1])

hb4List = df.iloc[:, [24,25]]
# print(ha1List)

hb4XValues = []
hb4YValues = []


for index in hb4List.index:
    for column in hb4List.columns:
            hb4XValues.append(hb4List[column][index]) if 'HB4' in column else hb4YValues.append(hb4List[column][index])

print(len(hb4XValues), len(hb4YValues))

data = {
    'X': hb4XValues, 'Y': hb4YValues
}


plt.scatter(hb4XValues, hb4YValues, s=10)
#plt.show()
plt.savefig('ha1scatter.png', dpi=300)

'''
sns.set_theme(style="whitegrid")
sns.color_palette("tab10")
f, ax = plt.subplots(figsize=(6.5, 6.5))
sns.despine(f, left=True, bottom=True)
sns.scatterplot(x='X', y='Y', data=data)
plt.show()
'''