import requests
from bs4 import BeautifulSoup as bf
import urllib
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns#(pip install seaborn)
import sqlite3#連結資料庫
import pymysql
import csv#將檔案存成csv檔
import datetime
#細部解說:https://ithelp.ithome.com.tw/articles/10234188
def _donload():
    myheaD = {'usue-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    urL_1='https://www.tfai.org.tw/boxOffice/weekly'
    rq_1 = requests.get(urL_1,headers=myheaD).text
    soup_1 =bf(rq_1,'lxml')
    soup_2 = soup_1.find('ul','download-list m-b-50')
    patH = r'C:\Users\USER\Desktop\資料夾\10周電影資料(0628)'
    n=1
    for i in soup_2.find_all('li'):
        h = i.find('div','download-link')
        #t = i.find('span','title').text.strip()[6:22]
        #print(t)
        if n<10:
            #print('https://www.tfai.org.tw')
            try:
                a = h.find('a','xls')['href'].strip()
            except:
                print('continue')
                continue
            #print('https://www.tfai.org.tw'+a)
            b = 'https://www.tfai.org.tw'+a
            t = i.find('span','title').text.strip()[11:16]
            t_1 =t.replace('/','')
            urllib.request.urlretrieve(b,patH+'\\'+t_1+'.xlsx')
            n=n+1
        elif n==10:
            print('儲存完成')
            break
        else:
            n=n+1
            print('error')

def _individual_move(c):
    page = 0
    n = 0
    list_0 = []
    list_2 = []
    
    for i in range(10):
        path = r'C:\Users\USER\Desktop\資料夾\10周電影資料(0628)'
        df = pd.read_excel(path + '\\' + str(9-i) + '.xlsx')
        dic = {}
        num = list(df["序號"])    
        
        for i in range(0, num[-1], 1):
            dic[df['中文片名'][i]] = i
        
        try:
            n = n + 1
            a =df.loc[dic[c]]['中文片名']
            b = int(df.loc[dic[c]]['銷售票數'].replace(',',''))
            d = int(df.loc[dic[c]]['累計銷售票數'].replace(',',''))
            e = int(df.loc[dic[c]]['上映院數'])
            list_1 = [n,a,b,d,e]
            list_0.append(list_1)
            #print(df.loc[dic[c]]['中文片名'])
            #print('銷售票數', df.loc[dic[c]]['銷售票數'])
            #print('累計銷售票數', df.loc[dic[c]]['累計銷售票數'])
            list_2.append('week  '+str(n))
        except:
            print('continue')
            continue
        
    DF = DataFrame(list_0, columns=['時間','中文片名', '銷售票數', '累計銷售票數','上映院數'], index=[list_2])
    
    return DF

def _lmplot(df):
    sns.set_theme(style="darkgrid")#背景風格
    sns.lmplot(data=df,x='時間', y="銷售票數",ci=None)

def _scatterplot(df):
    sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})#可以顯示中文
    cmap = sns.cubehelix_palette(rot=-0.7, as_cmap=True)
    #as_cmap=True:圖示是否重複
    #rot:顏色
    g = sns.relplot(
        data=df,
        x="時間", y="累計銷售票數",
        hue="銷售票數", size="上映院數",
        palette=cmap, sizes=(10, 200),#點的大小範圍
    )
    #g.set(xscale="log", yscale="log")#將值轉換成log
    g.ax.xaxis.grid(True, "minor", linewidth=.25)#圖表的x輔助線
    g.ax.yaxis.grid(True, "minor", linewidth=.25)#圖表的y輔助線
    g.despine(left=False, bottom=False)#表格底線

def _save_as_csv():
    csv_filE= open('news_1.csv','w',newline="",encoding="utf-8-sig")
    writeR=csv.writer(csv_filE)
    writeR.writerow(['時間','中文片名', '銷售票數', '累計銷售票數','上映院數'])
    for i in range(4):
        writeR.writerows(['時間','中文片名', '銷售票數', '累計銷售票數','上映院數'])
       

#mondays_this_year = get_all_mondays(2023)
#a = str(mondays_this_year[0])[5:10].replace('-','')
#print(a)
 

#_donload()
#~~~~~~~~~~~~~~~~~~~~~~
#a = str(input("名子"))
#DF_2 = _individual_move(a)
#~~~~~~~~~~~~~~~~~~~~~~
#_lmplot(DF_2) 
#_scatterplot(DF_2)

#print(DF_2['銷售票數'])