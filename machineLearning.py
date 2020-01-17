import pandas as pd
import csv
from pandas import DataFrame
from sklearn import tree
from matplotlib import pyplot
from pandas.plotting import scatter_matrix
<<<<<<< HEAD
=======
import re
>>>>>>> 3d85bdab9027784b923f52192dcfefcc75dd9407

#Wczytanie danych z pliku
def readCSV(path):
    df = pd.read_csv(path)   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
    return df

pathTOCSV = 'exportDataframe.csv'
df = readCSV(pathTOCSV)
tempTable = df
#print(df)
#Uogólnienie danych
orczyki = df['Chairlift']+df['T-bar']+df['Rope']
wyciagi = df['Aerial']+df['Circulating']+df['Chairlift']
#Dodanie nowych kolumn z danymi do tablicy
tempTable = tempTable.assign(Elevators=wyciagi, Lifts=orczyki)

#Usunięcie zbednych rekordów
tempTable=tempTable.drop(columns=['Sunkid', 'T-bar', 'Rope','Aerial', 'Circulating'])
#lenght= len(tempTable)

labels=[]

test= 5
#print(tempTable[1: 3])
for x in range(0, len(tempTable)):
    temp=0
    if((tempTable.loc[x, "Routes total"] > 50) & (tempTable.loc[x, "Elevation difference"] >= 500) & (tempTable.loc[x, "Lifts total"] >= 10) & (tempTable.loc[x, "Elevators"] >= 10 )& (tempTable.loc[x, "Lifts"] >= 5)):
       # print("zgodne")
        labels.append(1)
       # print(tempTable.loc[x, "Routes total"])
    else:
        labels.append(0)

scatter_matrix(tempTable)
<<<<<<< HEAD
pyplot.show()

=======
#pyplot.show()
>>>>>>> 3d85bdab9027784b923f52192dcfefcc75dd9407

clf = tree.DecisionTreeClassifier()
clf.fit(tempTable, labels)
###
class checkData: #sprawdzanie poprawności wprowadzonych danych,normalizacjam konwersja danych
    def __init__(self, data):
        self.data = data

    def getData(self): #sprawdzanie poprawności danych ( można użyć white-space , - .
        regex = "\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}"
        if re.search(regex, self.data):
            match = re.search(regex, self.data)
            return self.check() #jeśli nie jest w takiej samej formie co lista to check()
        else:
            return ("Podałeś błędne dane")

    def check(self): #konwersja
        regex = "\d{2,5},\d{2,5},\d{2,5},\d{2,5},\d{2,5},\d{2,5}"
        if re.search(regex, self.data):
            match = re.search(regex, self.data)
            return self.makeTable(self.data)
        else:
            print(("Konwersja danych... \n"))
            dict = [' ','-','.']
            df = self.data
            df = df.replace(' ', ',')
            df = df.replace('.', ',')
            df = df.replace('-', ',')
            return (self.makeTable(df))

    def makeTable(self, final): #tworzy tabele
        table = []
        setting = final.split(',')
        for x in setting:
            table.append(x)
            #Zamiana na inta
        for i in range(len(table)):
            table[i] = int(table[i])
        if(table[2] == (table[3]+table[4]+table[5])):
            return table
        else:
            return ("Podałeś błędne dane")

class InsertDataToCheck:
    def __init__(self, count):
        self.count = int(count)

    def doit(self):
        yourData = []
        count = self.count
        print(count)

dane = checkData(input(
    "Enter the slope parameters  \n Routes total, Elevation difference, Lifts total, Aerial, Circulating, Chairlift: \n"))
collectData= (dane.getData())
answer = clf.predict([collectData])
if(answer == 1):
    print('Your slope is great ')
else:
    print('Your slope is not great ')
print(collectData)
