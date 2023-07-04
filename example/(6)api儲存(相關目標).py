import requests
import json
import csv
import sqlite3#連結資料庫
import math #計算頁數
#import pymysql

mykeY = "80696437"
urlOMDB = "http://www.omdbapi.com/?s="

def _Page(i):#i:電影名
    movieName = "+".join(i.split())
    movieUrl = urlOMDB+movieName+"&apikey="+mykeY
    dictFile = json.loads(requests.get(movieUrl).text)
    totaL = int(dictFile["totalResults"])
    pageS = math.ceil(totaL/10)+1
    page_list=[]
    for i in range(pageS):
        page_list.append(i)
    return (page_list)

def _search(i,thisPage):#i:電影名--thisPage:頁數串列
    movieName = "+".join(i.split())  #將[super man]轉成[super+man]
    movieUrl_list=[]
    for i in thisPage:
        movieUrl = urlOMDB+movieName+"&apikey="+mykeY+"&page = "+str(i) 
        movieUrl_list.append(movieUrl)
    return movieUrl_list

def _store_by_json(i,j):#i:網址--j:電影名
    with open (j+'相關(s)'+".json","w",encoding = "utf-8")as filE:
        for k in i:
            dictFile = json.loads(requests.get(k).text)
            json.dump(dictFile,filE,ensure_ascii=False,indent=4)  
        return print("已將",j,'以json的方式儲存')

def _store_by_csv(i,j):#i:網址--j:電影名
    csv_filE= open(j+'相關(s)'+'.csv','w',newline="",encoding="utf-8-sig")
    writeR=csv.writer(csv_filE)
    writeR.writerow(["電影名稱","上映年分","電影海報網址"])
    for k in i:
        dictFile = json.loads(requests.get(k).text)
        for m in dictFile["Search"]:
            writeR.writerow((m['Title'],m["Year"],m["Poster"]))
    csv_filE.close()
    return print("已將",j,'以csv的方式儲存')

def _store_by_DBBrowser(i,j):#i:網址--j:電影名
    db = sqlite3.connect(j+'.db')
    db.execute("CREATE TABLE movie_1(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,time TEXT,Poster TEXT)")
    for k in i:
        dictFile = json.loads(requests.get(k).text)
        for m in dictFile["Search"]:
            roW =[m['Title'],m["Year"],m["Poster"]]
            db.execute("INSERT INTO movie_1 (name,time,Poster)VALUES(?,?,?)",roW)
    db.commit()
    return print("已將",j,'以DB Browser的方式儲存')


def _store_by_Mysql(i, j):#i:網址--j:電影名
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
            cursor.execute("DROP TABLE IF EXISTS movie")
            # Delete the existing data; without this line, the data will accumulate on top of the previous data
            # Create the table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS movie (
                id INT AUTO_INCREMENT PRIMARY KEY,
                電影名稱 CHAR(200),
                上映日 CHAR(200),
                票房 CHAR(200)
            )
            """
            cursor.execute(create_table_query)
            connection.commit()

            dictFile = json.loads(requests.get(i).text)
            roW = [dictFile['Title'], dictFile['Released'], dictFile['BoxOffice']]
            insert_query = "INSERT INTO movie (電影名稱, 上映日, 票房) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, roW)
            connection.commit()

    finally:
        # Close the database connection
        connection.close()
        return print("已將",j,'以Mysql的方式儲存')




    
moviE = input("請輸入英文電影名稱")
#print(_Page(moviE))
#print(_search(moviE,_Page(moviE)))


'''以json的方式儲存'''#i:網址--j:電影名
#_store_by_json(_search(moviE,_Page(moviE)),moviE )
'''以csv的方式儲存'''#i:網址--j:電影名
#_store_by_csv(_search(moviE,_Page(moviE)),moviE )
'''以DB Browser的方式儲存'''#i:網址--j:電影名
_store_by_DBBrowser(_search(moviE,_Page(moviE)),moviE)  
'''以Mysql的方式儲存''' #i:網址--j:電影名   
#_store_by_Mysql(_search(moviE),moviE ) 
#問題
#如何知道自己的檔案哪裡(指令碼)


