import os
import pandas as pd

from glob import glob
from helpers.menu_extractor import MenuExtractor

input_path = './data'
output_file = './data/raw_menu_data.csv'

if __name__ == '__main__':
    input_files = glob(os.path.join(input_path, '*.xls*'))
    print("Files to process: %d" % len(input_files))
    with open(output_file, 'w',  encoding='utf-8') as f:
        for fpath in input_files:
            print("\t%s" %fpath)
            mex = MenuExtractor(fpath)
            menu_data = mex.menus_combined
            menu_data['File'] = os.path.basename(fpath)
            menu_data.to_csv(f, header=False, index=False)
            del mex
    # Add a header to the csv file
    df = pd.read_csv(output_file)
    df.columns = ['Food', 'Weight', 'Price', 'Type', 'Key', 'Date', 'File']
    df.to_csv(output_file, index=False)
    print("Done.")
