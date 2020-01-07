import pandas as pd
import re
import requests
import matplotlib
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import ssl


url = "https://www.skiresort.info/best-ski-resorts/poland/"
print(url)
getpage = requests.get(url)
getpage_soup = BeautifulSoup(getpage.text, 'html.parser')
resort_urls = getpage_soup.findAll('a', {'class':'h3'})

print(type(resort_urls))
resort_urls = [i.text for i in resort_urls]
df = pd.Series(resort_urls)
df.to_frame()
print(df.at[49])
df = df.drop(df[df.index > 49].index)
df = df.str.replace('\d+.', '')
df = df.str.replace(' ', '_')
df = df.str.replace('-', '')
print(df)
