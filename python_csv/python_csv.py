# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:15:32 2022

@author: Patri
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

#read html
html=urlopen("https://en.wikipedia.org/wiki/Comma-separated_values").read()

#prettify it
soup = BeautifulSoup(html, features="html.parser")

#find the correct tags
text = soup.find('table',class_='wikitable').findNext('pre').text

#remove double quotes
text = text.replace('""','')

#check
print(text)

#write csv
f = open('my_csv.csv','w')
f.write(text)
f.close()