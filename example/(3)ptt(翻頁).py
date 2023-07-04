import requests#json爬蟲
import json#json爬蟲，將檔案存成json檔
from bs4 import BeautifulSoup as bf#bs4爬蟲
import csv#將檔案存成csv檔
from datetime import datetime#時間


myheaD={'usere-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
cookies = {'over18':'1'}

totaY=str(datetime.now())
daY=totaY[8:10]
#print(daY)
#rq_3.encoding='utf-8'#不知道為什麼不行
t=0

urL ='https://www.ptt.cc/bbs/Gossiping/index.html'


rq_3 = requests.get(urL,myheaD,cookies=cookies).text
souP = bf(rq_3,'lxml');




#找出前50最新文章
while True:
    rq_3 = requests.get(urL, myheaD, cookies=cookies).text
    souP = bf(rq_3, 'lxml')
    for i in souP.find_all('div', 'title'):
        if t > 50:
            break
        print(t, i.text.strip())
        t = t + 1
    urL = 'https://www.ptt.cc' + souP.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href']
    print('https://www.ptt.cc' + souP.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href'])
    if t > 50:
        break   
                 

'''
#找出今天的熱門文章
             
quota=100 
total_number=0
popular_number =0         

while quota > 0:
    rq_3 = requests.get(urL, myheaD, cookies=cookies).text
    souP = bf(rq_3, 'lxml')
    for i in souP.find_all('div', 'r-ent'):
        daY_1 = str(i.find('div', 'date').text)
        # print(daY_1[3:5])
        if daY_1[3:5] == daY:
            total_number = total_number + 1
            if i.find('div', 'nrec').text == '爆':
                popular_number = popular_number + 1
                t = t + 1
                print(t, i.find('div', 'title').text.strip())
                # print(i.find('div', 'nrec').text)
                daY_1 = str(i.find('div', 'date').text)
                # print(daY_1[3:5])
                print(urL)
                print('~' * 30)
        elif daY_1[3:5] != daY:
            quota = quota - 1
            continue
        else:
            print('error')
    urL = 'https://www.ptt.cc' + souP.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href']
    # print('https://www.ptt.cc'+souP.find('div','btn-group btn-group-paging').find_all('a')[1]['href'])
    if quota < 50:
        break

print(popular_number) 
print(total_number)              
'''          



#將'找出今天的熱門文章'變成函式(未完成)
'''
def _PTT(urL):
    global popular_number, total_number, quota, t
    rq_3 = requests.get(urL, myheaD, cookies=cookies).text
    souP = bf(rq_3, 'lxml')
    for i in souP.find_all('div', 'r-ent'):
        daY_1 = str(i.find('div', 'date').text)
        #print(daY_1[3:5])
        if daY_1[3:5] == daY:
            total_number = total_number + 1
            if i.find('div', 'nrec').text == '爆':
                popular_number = popular_number + 1
                t = t + 1
                print(t, i.find('div', 'title').text.strip())
                print(i.find('div','nrec').text)
                daY_1 = str(i.find('div', 'date').text)
                print(daY_1[3:5])
                print(urL)
                print('~' * 30)
            else:
                print('error-1')
        elif daY_1[3:5] != daY:
            quota = quota - 1
            continue
        else:
            print('error-2')

    if quota <= 0:
        return None
    elif quota < 0:
        urL = 'https://www.ptt.cc' + souP.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href']
        return urL
    else:
        print('error-3')



myheaD={'usere-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
cookies = {'over18':'1'}

totaY=str(datetime.now())
daY=totaY[8:10]
#print(daY)
#rq_3.encoding='utf-8'#不知道為什麼不行
t=0

urL ='https://www.ptt.cc/bbs/Gossiping/index.html'


quota=100 
total_number=0
popular_number =0

while urL:
    urL=_PTT(urL)
'''