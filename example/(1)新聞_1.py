import requests#json爬蟲
import json#json爬蟲，將檔案存成json檔
from bs4 import BeautifulSoup#bs4爬蟲
import csv#將檔案存成csv檔

myHead={'usere-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

#聯合電子報
urL ="https://paper.udn.com/papers.php?pname=PID0001"
rq_1=requests.get(urL)
rq_1.encoding='utf-8'
bs_1= BeautifulSoup(rq_1.text,'html5lib')

#取得標題
print(bs_1.title.getText())

newS = {}

#聯合電子報
for i in bs_1.find_all('div','history_list'):
    for j in i.find_all('li','subject'):
        key=j.text.strip()
        value_1=j.a['href']
    for j in i.find_all('li','date'):
        value_2=j.text
        newS[key]=[value_1,value_2]
       

for i,j in newS.items():
    print(i)
    print(j)
    print("~~"*20)


