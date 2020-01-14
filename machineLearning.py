import pandas as pd
import csv
from pandas import DataFrame
from sklearn import tree
#Wczytanie danych z pliku
df = pd.read_csv (r'C:\Users\Mass\Desktop\\git\export_dataframe.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
tempTable =df

#Uogólnienie danych
orczyki = df['Chairlift']+df['T-bar']+df['Rope']
wyciagi = df['Aerial']+df['Circulating']+df['Chairlift']
#Dodanie nowych kolumn z danymi do tablicy
tempTable = tempTable.assign(Elevators=wyciagi, Lifts=orczyki)

#Usunięcie zbednych rekordów
tempTable=tempTable.drop(columns=['Sunkid', 'T-bar', 'Rope','Aerial', 'Circulating'])
lenght= len(tempTable)

labels=[]

test= 5
#print(tempTable[1: 3])
for x in range(lenght):
    temp=0
    if((tempTable.loc[x, "Routes total"] > 50) & (tempTable.loc[x, "Elevation difference"] >= 500) & (tempTable.loc[x, "Lifts total"] >= 10) & (tempTable.loc[x, "Elevators"] >= 10 )& (tempTable.loc[x, "Lifts"] >= 5)):
       # print("zgodne")
        labels.append(1)
       # print(tempTable.loc[x, "Routes total"])
    else:
        labels.append(0)

clf = tree.DecisionTreeClassifier()
clf.fit(tempTable, labels)

print(clf.predict([[10, 600, 5, 4,10,1],[60, 1000, 19, 10, 9,2]]))

