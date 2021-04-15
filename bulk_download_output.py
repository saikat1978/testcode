import pandas as pd
import sys
import urllib.request as request
import os
import asyncio
import logging


logging.basicConfig(level=logging.NOTSET)


async def download(url, serial, filepath):
    request.urlretrieve(url, filepath)
    logging.info(f'{serial} downloaded')


async def read_df(file, sheet):
    logging.info('inside read_df')
    
    df = pd.read_excel (file, sheet_name=sheet)
    df = pd.DataFrame(df, columns= ['SN', 'Img URL'])
    
    folder = os.path.join('outputs', sheet)
    
    if not os.path.exists(folder):
        os.mkdir(folder)
        logging.info(folder + ' created')
    
    for ind in df.index:
        url = str(df['Img URL'][ind])
        serial = df['SN'][ind]
        try:
            await download(url, serial, os.path.join(folder, str(serial) + '.png'))
        except:
            logging.info(f'{serial} error occurred')
    


if __name__ == '__main__':
    file = sys.argv[1]
    sheet = sys.argv[2]
        
    asyncio.run(read_df(file, sheet))
    logging.info('downloaded files')