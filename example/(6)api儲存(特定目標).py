import requests
import json
import csv
import sqlite3#連結資料庫
import pymysql

def _search(i):
    mykeY = "80696437"
    urlOMDB = "http://www.omdbapi.com/?t="
    movieName = "+".join(i.split())  #將[super man]轉成[super+man]
    movieUrl = urlOMDB+movieName+"&apikey="+mykeY
    return movieUrl

def _store_by_json(i,j):
    dictFile = json.loads(requests.get(i).text)
    with open (j+"(t).json","w",encoding = "utf-8")as filE:
        json.dump(dictFile,filE,ensure_ascii=False,indent=4)
        return print("已將",j,'以json的方式儲存')

def _store_by_csv(i,j):
    dictFile = json.loads(requests.get(i).text)
    csv_filE= open(j+'.csv','w',newline="",encoding="utf-8-sig")
    writeR=csv.writer(csv_filE)
    writeR.writerow(["電影名稱","上映日","票房"])
    writeR.writerow((dictFile['Title'],dictFile['Released'],dictFile['BoxOffice']))
    csv_filE.close()
    return print("已將",j,'以csv的方式儲存')

def _store_by_DBBrowser(i,j):
    dictFile = json.loads(requests.get(i).text)
    db = sqlite3.connect(j+'.db')
    roW = [dictFile['Title'],dictFile['Released'],dictFile['BoxOffice']]
    db.execute("CREATE TABLE movie(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,time TEXT,BoxOffice TEXT)")
    db.execute("INSERT INTO movie (name,time,BoxOffice)VALUES(?,?,?)",roW)
    db.commit()
    return print("已將",j,'以DB Browser的方式儲存')


def _store_by_Mysql(i, j):
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

'''以json的方式儲存'''
#_store_by_json(_search(moviE),moviE )
'''以csv的方式儲存'''
#_store_by_csv(_search(moviE),moviE )
'''以DB Browser的方式儲存'''
#_store_by_DBBrowser(_search(moviE),moviE )  
'''以Mysql的方式儲存'''     
_store_by_Mysql(_search(moviE),moviE ) 
