from typing import Any
import pandas as pd
import sys
import os
import math
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
import seaborn as sns


typeMap = {
    1: 'Hook-WaterStain', 2: 'Polygon', 3: 'SymmetryMoon'
}
plt.ioff()
def generateImage(typeInfo: int, inputFolderLoc: str):
    outputFolder = os.path.join(os.getcwd(), typeMap[typeInfo])

    if os.path.exists(outputFolder) and os.path.isdir(outputFolder):
        for file in os.listdir(outputFolder):
            os.remove(f'{outputFolder}/{file}')
        os.removedirs(outputFolder)
    
    os.mkdir(outputFolder)
    
    csvFolderLoc = os.path.join(inputFolderLoc, 'CSV')
    files = os.listdir(csvFolderLoc)
    
    for csvFile in files:
        print(f'processing {csvFile}')
        df = pd.read_csv(os.path.join(csvFolderLoc, csvFile), header=[0, 1])
        df.dropna(how='all', axis=1, inplace=True)
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
            
        plt.scatter(largestDf[largestDf.columns[0]].tolist(), 
            largestDf[largestDf.columns[1]].tolist(), s=2) 
        plt.savefig(os.path.join(outputFolder, os.path.splitext(csvFile)[0] + '.png'), dpi=600)  
        plt.close()


if __name__=='__main__':
    typeInfo = int(sys.argv[1])
    folderPath = sys.argv[2]
    generateImage(typeInfo, folderPath)