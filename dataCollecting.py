import pandas as pd
import unidecode
import re
import requests
import matplotlib
import matplotlib.pyplot as plt
import soup as soup
from bs4 import BeautifulSoup
import ssl


urls = ["https://www.skiresort.info/best-ski-resorts/poland/", "https://www.skiresort.info/best-ski-resorts/austria/", "https://www.skiresort.info/best-ski-resorts/germany/", "https://www.skiresort.info/best-ski-resorts/united-kingdom/" ,"https://www.skiresort.info/best-ski-resorts/italy/"]

class makeDfOfAreas:
    def __init__(self, urls):
        self.urls = urls

    def __makeDFWithAreas(self, url):
        getpage = requests.get(url)
        getpage_soup = BeautifulSoup(getpage.text, 'html.parser')
        resort_urls = getpage_soup.findAll('a', {'class':'h3'})
        #print(type(resort_urls))
        resort_urls = [i.text for i in resort_urls]
        df = pd.Series(resort_urls)
        df.to_frame()
        #print(df.at[49])
        df.columns = ['area']
        df = df.drop(df[df.index > 49].index)
        df = df.str.lower()
        df = df.str.replace('\d+.\s', '')
        df = df.str.replace('\s$', '')
        df = df.str.replace('  ', '')
        df = df.str.replace('/', '')
        df = df.str.replace(' ', '-')
        df = df.str.replace('–-', '')
        df = df.str.replace('(', '')
        df = df.str.replace(')', '')
        df = df.str.replace('.', '')
        df = df.str.replace('ö', 'o')
        df = df.str.replace('ä', 'a')
        df = df.str.replace('ü', 'u')
        df = df.str.replace('ä', 'a')
        df = df.str.replace('ß', 's')
        df = df.str.replace('ą', 'a')
        df = df.str.replace('ę', 'e')
        df = df.str.replace('ć', 'c')
        df = df.str.replace('ł', 'l')
        df = df.str.replace('ń', 'n')
        df = df.str.replace('ó', 'o')
        df = df.str.replace('ś', 's')
        df = df.str.replace('ż', 'z')
        df = df.str.replace('ź', 'z')

        return df

    def appendingAreasNames(self):
        df = pd.DataFrame()
        for site in urls:
            df = pd.concat([df , self.__makeDFWithAreas(site)])
        df = df.rename(columns={0: 'areas' })
        return df


dfOfAreas = makeDfOfAreas(urls)

print(dfOfAreas.appendingAreasNames())



