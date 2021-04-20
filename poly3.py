from typing import Any
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
#print(len(df.columns))
df.dropna(how='all', axis=1, inplace=True)
#print(len(df.columns))

dataSize = 0
largestDataIndex = 0
largestDf = Any

for i in range(0, len(df.columns), 2):
    dataList = df.iloc[:, [i, i+1]]
    dataList = dataList.dropna()
    dataList = dataList.reset_index(drop=True)
    #print(f'index = {i}')
    #print(dataList)
    
    size = len(dataList.index)
    if size > dataSize:
        dataSize = size
        largestDataIndex = i
        largestDf = dataList
        print(f'data size = {dataSize}, largest index = {largestDataIndex}')
    
    
        

#print(dataSize, largestDataIndex)
#print(largestDf)

plt.scatter(largestDf[largestDf.columns[0]].tolist(), largestDf[largestDf.columns[1]].tolist(), s=2)
plt.show()

'''
sns.set_theme(style="whitegrid")
sns.color_palette("tab10")
f, ax = plt.subplots(figsize=(6.5, 6.5))
sns.despine(f, left=True, bottom=True)
sns.scatterplot(x=largestDf.columns[0], y=largestDf.columns[1], data=largestDf)
plt.show()
'''
