import pandas as pd
import os
import sys
import matplotlib.pyplot as plt


file = sys.argv[1]

df = pd.read_csv(file, header=[0, 1])
df.dropna(how='all', axis=1, inplace=True)
print(df)

xlist = []
ylist = []

for i in range(0, len(df.columns), 2):
    dataList = df.iloc[:, [i, i+1]]
    dataList = dataList.dropna()
    dataList = dataList.reset_index(drop=True)
    xlist.extend(dataList[dataList.columns[0]].tolist())
    ylist.extend(dataList[dataList.columns[1]].tolist())


print(len(xlist), len(ylist))
plt.scatter(xlist, ylist, s=2)
plt.savefig('random.png')