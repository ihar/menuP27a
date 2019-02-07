import os

from glob import glob
from helpers.menu_extractor import MenuExtractor

input_path = './data'
output_file = 'menu_data.csv'

if __name__ == '__main__':
    input_files = glob(os.path.join(input_path, '*.xls*'))
    print("Files to process: %d" % len(input_files))
    with open(output_file, 'w',  encoding='utf-8') as f:
        for fpath in input_files:
            mex = MenuExtractor(fpath)
            menu_data = mex.menus_combined
            menu_data['File'] = os.path.basename(fpath)
            menu_data.to_csv(f, header=False, index=False)
            del mex
    print("Done.")
