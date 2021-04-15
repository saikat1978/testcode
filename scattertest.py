import pandas as pd
import sys
import os
import math
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


csvFile = sys.argv[1]

df = pd.read_csv(csvFile, header=[0, 1])

ha1List = df.iloc[:, [0,1]]
# print(ha1List)

ha1XValues = []
ha1YValues = []


for index in ha1List.index:
    for column in ha1List.columns:
            ha1XValues.append(ha1List[column][index]) if 'HA1' in column else ha1YValues.append(ha1List[column][index])

print(len(ha1XValues), len(ha1YValues))

plt.scatter(ha1XValues, ha1YValues)
plt.savefig('ha1scatter.png', dpi=300)
