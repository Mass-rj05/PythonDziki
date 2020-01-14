import pandas as pd
import csv
from pandas import DataFrame

df = pd.read_csv (r'C:\Users\Mass\Desktop\\git\export_dataframe.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
print (df)