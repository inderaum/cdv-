
import pandas as pd
import codecs

'''Escape special characters in a given csv file'''


def escape_special_characters():
    with codecs.open('../data/raw_data.csv', 'r', encoding='latin1', errors='ignore') as csv:
        raw_data = pd.read_csv(csv, sep=';', error_bad_lines=True)
        for column in raw_data:
            print(column)
            if pd.isna(column[1]):
                print("NaN found")

escape_special_characters()
