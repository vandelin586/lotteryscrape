from sys import displayhook
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
df = pd.read_csv(
    'fivelist.txt',header=None)
print(df)
