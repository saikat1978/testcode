import pandas as pd
import os
import sys
import matplotlib.pyplot as plt


typeMap = {
    1: 'IRIS01-Hook-WaterStain-PreSput', 2: 'IRIS02-Polygon-SCR-Wash', 3: 'IRIS03-SymmetryMoon-AlODroplet-Sub'
}

BASE_DIR = '/Users/sc1000255563/Documents/SZ-IRIS/prescribed'

def generate(infolder, outfolder):
    
    infiles = os.listdir(infolder)
    
    for file in infiles:
        print(file)
        df = pd.read_csv(f'{infolder}/{file}', header=[0, 1])
        df.dropna(how='all', axis=1, inplace=True)
        #print(df)

        AXlist = []
        AYlist = []
        
        BXlist = []
        BYlist = []

        for i in range(0, len(df.columns), 2):
            dataList = df.iloc[:, [i, i+1]]
            dataList = dataList.dropna()
            dataList = dataList.reset_index(drop=True)
            print(dataList.columns[0], 'A side ' if 'HA' in str(dataList.columns[0]) else 'B side')
            if 'HA' in str(dataList.columns[0]):
                AXlist.extend(dataList[dataList.columns[0]].tolist())
                AYlist.extend(dataList[dataList.columns[1]].tolist())
            else:
                BXlist.extend(dataList[dataList.columns[0]].tolist())
                BYlist.extend(dataList[dataList.columns[1]].tolist())

        #print(len(xlist), len(ylist))
        plt.scatter(AXlist, AYlist, s=2)
        outname, ext = os.path.splitext(file)
        plt.gca().set_aspect('equal')
        plt.savefig(f'{outfolder}/{outname}_A.png', dpi=600)
        plt.close()
        
        plt.scatter(BXlist, BYlist, s=2)
        plt.gca().set_aspect('equal')
        plt.savefig(f'{outfolder}/{outname}_B.png', dpi=600)
        plt.close()
        

    


if __name__ == '__main__':
    defectType = int(sys.argv[1])
    infolder = typeMap[defectType]
    outfolder = os.getcwd() + f'/{infolder}'
    infolder = f'{BASE_DIR}/{infolder}/CSV'
    print(f'path is {infolder}')
    
    print(f'output = {outfolder}')
    
    if not os.path.exists(outfolder):
        os.mkdir(outfolder)
    generate(infolder, outfolder)
    