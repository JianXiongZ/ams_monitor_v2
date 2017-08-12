#!/usr/bin/env python3
# encoding: utf-8
from urllib.request import urlopen
# from bs4 import BeautifulSoup
from urllib.parse import quote
from io import StringIO
import csv
import urllib.request

x = []
y = []


def request_data(farm):
    info = []
    url = "https://monitor.makai.moe/miao/" + quote(farm) + ".csv"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    data = urlopen(req).read().decode('ascii', 'ignore')
    datafile = StringIO(data)
    csvReader = csv.reader(datafile)

    for row in csvReader:
        info.append(row)
    
    return info[-144::]
    

result = request_data('老安统')
print(result)
