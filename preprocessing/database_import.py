import pandas as pd
import codecs
import re

'''Escape special characters in a given csv file'''


def escape_special_characters():
    with codecs.open('../data/raw_data.csv', 'r', encoding='latin1', errors='ignore') as csv:
        raw_data = pd.read_csv(csv, sep=';', error_bad_lines=True,
                               dtype={"AUS": object,
                                      "LP_NR": int,
                                      "SEITE": object,
                                      "TITEL_NR": int,
                                      "ART": str,
                                      "LPTITEL": str,
                                      "TITEL": str,
                                      "BAND": str,
                                      "DIRIGENT": str,
                                      "KOMPONIST": str,
                                      "INTERPR1": str,
                                      "INTERPR2": str,
                                      "INTERPR3": str,
                                      "INTERPR4": str,
                                      "INTERPR5": str,
                                      "INTERPR6": str,
                                      "INTERPR7": str,
                                      "INTERPR8": str,
                                      "INTERPR9": str,
                                      "INTERPR10": str,
                                      "ANMERKUNG": str,
                                      "MUSIKART": str,
                                      "JAHR": int,
                                      "MIN": int,
                                      "NOTE": object,
                                      "SEK": int,
                                      "WAHL": int})

        for column in raw_data:
            if raw_data[column].dtype == 'object':
                raw_data[column] = raw_data[column].str.replace('"', '\\"')

        raw_data.to_csv('../data/escaped_data.csv', sep=';', encoding='latin1', na_rep=0)


# escape_special_characters()