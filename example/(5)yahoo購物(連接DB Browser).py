import requests
from bs4 import BeautifulSoup as bf
import os
import urllib
import sqlite3#連結資料庫
#db.close()
##關資料庫之指令
#conN = sqlite3.connect()
#conN.execute()#一定要和close一起
#conN.commit()#資料儲存
#conN.close()
#解決抓不到的問題
#https://www.learncodewithmike.com/2020/09/7-tips-to-avoid-getting-blocked-while-scraping.html

db = sqlite3.connect('手機殼'+'.db')
db.execute("CREATE TABLE goods(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,price NUMRRIC,url TEXT)")
db.commit()

myheaD = {'usue-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
urL_1='https://tw.buy.yahoo.com/search/product?p=iphone%2013%20%E4%BF%9D%E8%AD%B7%E6%AE%BC'
rq_1 = requests.get(urL_1,headers=myheaD).text
soup_1 =bf(rq_1,'lxml')
soup_2= soup_1.find('div','ResultList_resultList_IpWJt')

for i in soup_2.find_all('a'):
    a = i['href']
    b = i.find('span','sc-ispOId sc-kcuKUB sc-hCnrGf byTypU ercMzW hXvLDl')
    c = i.find('div','sc-pDgPE hntwsh')
    try:
        roW = []
        roW.append(b.text)
        roW.append(c.text)
        roW.append(a)
        db.execute("INSERT INTO goods (name,price,url)VALUES(?,?,?)",roW)
        db.commit()
        print(roW)
    except:
        continue
  
db.close()    

