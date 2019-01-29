import urllib3
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import MeCab
#import urllib2

url = 'https://www.uta-net.com/artist/994/'
contents = []
bsURL = requests.get(url)
soup = BeautifulSoup(bsURL.text, 'html.parser')
song_url = soup.find_all('a', href=re.compile('/song/'))
contents.append(soup.find_all('a', href=re.compile('/song/')))
#print(str(song_url))
infomations = []
for i, content in enumerate(contents):
    url_list = []
    for element in content:
        if i == 0:
            url_list.append(element.get('href'))
        else:
            url_list.append(element.string)
    infomations.append(url_list)
#print(url_list)
artist_df = pd.DataFrame({
    'URL' : infomations[0]})

artist_df.URL = artist_df.URL.apply(lambda x : 'https://www.uta-net.com' + x)
print(artist_df)

contents_list = []
for i, url in artist_df.URL.iteritems():
    contents_list.append(url)
#print("check1"contents_list[0])
lyrics = []

#print(contents)
#bsURL2 = requests.get(contents_list[0])
#soup2 = BeautifulSoup(bsURL2.text, 'html.parser')

for contents in contents_list:
    bsURL2 = requests.get(contents_list[len(contents)])
    soup2 = BeautifulSoup(bsURL2.text, 'html.parser')
   # print(soup2.find(id='kashi_area'))
    lyrics.append(soup2.find(id='kashi_area'))
print(lyrics)
#print("check2"lyrics[0])

path = 'kashi.txt'
for zero in lyrics:
#    print(zero)
    file = open(path, 'a')
    file.write(str(zero))
    file.close()
