import pandas as pd
import re
import requests
import matplotlib
import matplotlib.pyplot as plt
import soup as soup
from bs4 import BeautifulSoup
import ssl


urls = ["https://www.skiresort.info/best-ski-resorts/poland/", "https://www.skiresort.info/best-ski-resorts/austria/", "https://www.skiresort.info/best-ski-resorts/germany/","https://www.skiresort.info/best-ski-resorts/united-kingdom/"]

df = pd.DataFrame()

def makeDFWithAreas(url):
    getpage = requests.get(url)
    getpage_soup = BeautifulSoup(getpage.text, 'html.parser')
    resort_urls = getpage_soup.findAll('a', {'class':'h3'})
    #print(type(resort_urls))
    resort_urls = [i.text for i in resort_urls]
    df = pd.Series(resort_urls)
    df.to_frame()
    #print(df.at[49])
    df = df.drop(df[df.index > 49].index)
    df = df.str.replace('\d+.\s', '')
    df = df.str.replace('\s$', '')
    df = df.str.replace('  ', '')
    df = df.str.replace('/', '')
    df = df.str.replace(' ', '-')
    df = df.str.replace('–-', '')
    df = df.str.replace('(', '')
    df = df.str.replace(')', '')
    return df


print(type(makeDFWithAreas(urls[1])))

for site in urls:
    print(site)
    df.append(makeDFWithAreas(site), ignore_index= True)

print(df)










