import os
import pandas as pd
import hashlib

from glob import glob
from helpers.menu_extractor import MenuExtractor

input_path = './data'
output_file = './data/raw_menu_data.csv'


def sha1sum(filename):
    h = hashlib.sha1()
    b = bytearray(128 * 1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda: f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()


def select_new_files(input_files, output_file):
    """
    List Excel files in the input_path folder and return only files
    that haven't processed yet according SHA1 column in the output_file
    :param input_path: a list of paths to Excel menu files
    :param output_file: a path to a csv files with existing extracted data
    :return: a list of paths to Excel files that haven't processed yet
    """
    new_files = []
    try:
        df = pd.read_csv(output_file)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        print("Provided CSV files either does not exist or empty.")
        return input_files
    try:
        existed_sha1 = df['SHA1'].unique()
    except KeyError:
        print("SHA1 column does not exist in the provided CSV file.")
        return input_files
    for fpath in input_files:
        sha1 = sha1sum(fpath)
        if sha1 not in existed_sha1:
            new_files.append(fpath)
    return new_files


def main():
    input_files = glob(os.path.join(input_path, '*.xls*'))
    print("Files to process: %d" % len(input_files))
    input_files = select_new_files(input_files, output_file)
    print("New files: %d" % len(input_files))
    if 0 == len(input_files):
        print("There is nothing to add to the existing CSV file.")
        return
    with open(output_file, 'a',  encoding='utf-8') as f:
        for fpath in input_files:
            print("\t%s" % fpath)
            mex = MenuExtractor(fpath)
            menu_data = mex.menus_combined
            menu_data['File'] = os.path.basename(fpath)
            menu_data['SHA1'] = sha1sum(fpath)
            menu_data.to_csv(f, header=False, index=False)
            del mex
    # Add a header to the csv file
    df = pd.read_csv(output_file)
    df.columns = ['Food', 'Weight', 'Price', 'Type', 'Key', 'Date', 'File', 'SHA1']
    df.to_csv(output_file, index=False)
    print("Done.")


if __name__ == '__main__':
    main()
