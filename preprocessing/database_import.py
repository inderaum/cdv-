import pandas as pd
import codecs

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
        avg_col = raw_data.groupby(["MUSIKART", "JAHR"]).median()
        # print(avg_col.loc["BLUES",1977])
        for cell in raw_data.iteritems():
            # if cell[1]==1977:
            print(cell[1])


escape_special_characters()
