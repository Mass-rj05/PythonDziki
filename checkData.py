import re

class checkData: #sprawdzanie poprawności wprowadzonych danych,normalizacjam konwersja danych
    def __init__(self, data):
        self.data = data

    def getData(self): #sprawdzanie poprawności danych ( można użyć white-space , - .
        regex = "\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}[\s,-\.]\d{2,5}"
        if re.search(regex, self.data):
            match = re.search(regex, self.data)
            #można dać if że jeśli ilość wyciagow łącznie < od wycaig+orczyk+tasma
            return self.check() #jeśli nie jest w takiej samej formie co lista to check()
        else:
            return ("Podałeś błędne dane")

    def check(self, ): #konwersja
        regex = "\d{2,5},\d{2,5},\d{2,5},\d{2,5},\d{2,5},\d{2,5}"
        if re.search(regex, self.data):
            match = re.search(regex, self.data)
            return self.makeTable()
        else:
            print(("Konwersja danych... \n"))
            dict = ['.',' ','-']
            for x in range(len(dict)):
               final = self.data.replace(dict[x], ',')
            return (self.makeTable(final))

    def makeTable(self, final): #tworzy tabele
        setting = final.split(' ')
        table=[]
        for x in setting:
            table.append(x)
        return table


# [,-\.\s]\d[1-5][,-\.\s]\d[1-5][,-\.\s]\d[1-5][,-\.\s]\d[1-5]

# print(download.downloadData(areasSizeList, listOfValidateNumbers))

dane = checkData(input(
    "Enter the slope parameters  \n 'Routes total', 'Elevation difference', 'Lifts total', ['Aerial'], ['Circulating'], ['Chairlift']: \n"))

w= (dane.getData())
print(w[1])