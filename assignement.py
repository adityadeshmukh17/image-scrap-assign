import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging
import os
import csv
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
response=requests.get("https://www.youtube.com/@PW-Foundation/videos")
soup=BeautifulSoup(response.content,"html.parser")
print(soup)
imagetags=soup.find_all("div",{"class":"style-scope ytd-rich-grid-media"})
del imagetags[0:5]
print(len(imagetags))
a,b,c,d=[]
for j in range(5):
    a.append("https://www.youtube.com/"+imagetags[j].a['href'])
    b.append(imagetags[j].a["title"])
    c.append(imagetags[j].div.div.span["class":"inline-metadata-item-style-scope-ytd-video-meta-block"].text)
    d.append(imagetags[j].div.div.span.span["class":"inline-metadata-item-style-scope-ytd-video-meta-block"].text)
e=[]
for j in range(4):
    e.append(a)
    e.append(b)
    e.append(c)
    e.append(d)

with open ('data.csv','w') as f:
    s=csv.writer(f)
    for i in e:
        s.writerow(i)
# print(imagetags[0])




