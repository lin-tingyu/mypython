import requests
from bs4 import BeautifulSoup as bf
import urllib
import pandas as pd
import sqlite3#連結資料庫
import pymysql
import datetime
from pandas import Series, DataFrame
import time
import seaborn as sns#(pip install seaborn)
import matplotlib.pyplot as plt

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


def get_all_mondays(year):
    n=1
    week = DataFrame(columns=['monday','week_num'],index=[i for i in range(1,54)])
    date = datetime.date(year, 1, 1)
    # Iterate through all the days in the year
    while date.year == year:
        if date.weekday() == 0:  # Monday is represented by 0
            date_1 = str(date)[5:].replace('-','')
            week['monday'][n] = date_1
            week['week_num'][n] = n
            n=n+1
        date += datetime.timedelta(days=1)
    return week

def _xlsx_save_mysql(w):
    week= get_all_mondays(2023)     
    w_now = int(time.strftime('%W'))
    for k in range(w+1,1,-1):
        patH_1 = r'C:\Users\USER\Desktop\資料夾\10周電影資料(0628)'
        patH_2 = week['monday'][(w_now-k)]
        
        dictFile = pd.read_excel(patH_1+'\\'+patH_2+'.xlsx')
            # Establish a connection to the MySQL database
        db_settings = {
                "host": "127.0.0.1",
                "port": 3306,
                "user": "root",
                "password": "1234",
                "db": "python_test",
                "charset": "utf8"
            }
        connection = pymysql.connect(**db_settings) 
        try:
            with connection.cursor() as cursor:
                #cursor.execute("DROP TABLE IF EXISTS originaL_datA")
                create_table_query = """
                CREATE TABLE IF NOT EXISTS originaL_datA (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    周      FLOAT,
                    資料時間 CHAR(200),
                    電影名稱 CHAR(200),
                    銷售票數 FLOAT,
                    上映院數 FLOAT,
                    累計銷售票數 FLOAT
                )
                """
                cursor.execute(create_table_query)
                connection.commit()
                for i in range(dictFile.shape[0]):
                    a = float(w_now-k)
                    b = week['monday'][(w_now-k)]
                    c = dictFile['中文片名'][i]
                    d = float(str(dictFile['銷售票數'][i]).replace(',',''))
                    e = float(str(dictFile['上映院數'][i]).replace(',',''))
                    f = float(str(dictFile['累計銷售票數'][i]).replace(',',''))
                    roW = [a,b,c,d,e,f]
                    #print(roW)
                    insert_query = "INSERT INTO originaL_datA ( 周,資料時間, 電影名稱, 銷售票數,上映院數,累計銷售票數) VALUES (%s,%s, %s, %s, %s ,%s)"
                    cursor.execute(insert_query, roW)
                    connection.commit()   
        finally:
            # Close the database connection
            connection.close()
        
        print('originaL_datA  已經儲存')
        
def _call_xlsx():
    # MySQL connection information
    db_settings = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "1234",
        "db": "python_test",
        "charset": "utf8"
    }

    # Establish a connection to the MySQL database
    connection = pymysql.connect(**db_settings)

    try:
        # Query to select all rows from the table
        select_query = "SELECT * FROM originaL_datA"

        # Read data from MySQL into a pandas DataFrame
        df_1 = pd.read_sql(select_query, connection)
    finally:
        # Close the database connection
        connection.close()
    return(df_1)

def _individual_move(c):
    df = DataFrame(_call_xlsx())
    print(df[df.電影名稱 == a])

def _lmplot(a):
    df = DataFrame(_call_xlsx())
    df_2 = df[df.電影名稱 == a]
    print(df_2)
    sns.set_theme(style="darkgrid")#背景風格
    sns.lmplot(data=df_2 ,x='周', y="銷售票數",ci=None)

def _scatterplot(a):
    df = DataFrame(_call_xlsx())
    df_2 = df[df.電影名稱 == a]
    print(df_2)
    sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})#可以顯示中文
    cmap = sns.cubehelix_palette(rot=-0.7, as_cmap=True)
    #as_cmap=True:圖示是否重複
    #rot:顏色
    g = sns.relplot(
        data=df_2,
        x="周", y="累計銷售票數",
        hue="銷售票數", size="上映院數",
        palette=cmap, sizes=(10, 400),#點的大小範圍
    )
    #g.set(xscale="log", yscale="log")#將值轉換成log
    g.ax.xaxis.grid(True, "minor", linewidth=.25)#圖表的x輔助線
    g.ax.yaxis.grid(True, "minor", linewidth=.25)#圖表的y輔助線
    g.despine(left=False, bottom=False)#表格底線


#_donload()
#w = int(input('輸入週數(1~9間)'))
#_xlsx_save_mysql(w) 


#a = str(input("名子")) 
#_lmplot(a)
#_scatterplot(a)
      
a = str(input("名子")) 
#_lmplot(a)
#plt.show()#notepade++ & cmd 要加這行，表格才會出現
_scatterplot(a)
plt.show()#notepade++ & cmd要加這行，表格才會出現       

