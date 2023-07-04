import requests
from bs4 import BeautifulSoup as bf
import urllib
import os
from datetime import datetime#時間


myheaD = {'usue-agent':'"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
urL = 'https://www.ptt.cc/bbs/Beauty/index.html'

cookies = {'over18':'1'}
rq_1 = requests.get(urL,myheaD,cookies=cookies).text
souP =  bf(rq_1,'lxml')
totaY=str(datetime.now())
#daY=str(int(totaY[8:10]))
daY='4'
#daY='10'


#print(souP.title.getText()[:9])
#next_page ='https://www.ptt.cc'+souP.find('div','btn-group btn-group-paging').find_all('a','btn wide')[1]['href'])

n=0
nm=300


def _copy(j, i):
    rq_2 = requests.get(i, myheaD, cookies=cookies).text
    souP = bf(rq_2, 'lxml')

    if not os.path.exists(j):
         os.mkdir(j)
         for i in souP.find_all('div', 'richcontent'):
            if i.find('img') is not None:
                #print(type(i.find('img')))
                linK = i.find('img')['src']
                print(linK)
                a = i.find('img')['src'].split('/')[-1]
                pic_name = a.split('?')[0]
                try:
                     urllib.request.urlretrieve(linK, j+'\\'+pic_name)
                except:
                     print('error-1')
            else:print('None')
    elif os.path.exists(j):
        print('此已儲存過')
    else:
        print('error')

_copy('[正妹]','https://www.ptt.cc/bbs/Beauty/M.1686470166.A.345.html')


'''
def _copy_2(j,i):    
    rq_2 = requests.get(i,myheaD,cookies=cookies).text
    souP =  bf(rq_2,'lxml')
    
    if not os.path.exists(j):
        #os.mkdir(j)
        souP_f1 = souP.find('div','bbs-screen bbs-content')
        souP_f2 = souP_f1.find_all('a')
        for i in souP_f2:
            linK = i['href']
            pic_name = i['href'].split('/')[-1]
            cookies_1 = {'is_authed':'1'}
            rq_3=requests.get(linK,myheaD,cookies=cookies_1).text
            souP_3 = bf(rq_3,'lxml')
            print(souP_3.title.getText())
            #linK_2=souP_3.find('div','Gallery-Content--mediaContainer')
            
            #print(linK_2)
            #pic_name = linK.split('/')[-1]
            #try:
                #urllib.request.urlretrieve(linK_2,j+'\\'+pic_name)
            #except:
            #    print('error-1')
    elif os.path.exists(j):
        print('此已儲存過')
    else:
        print('error')

#這個還未解
_copy_2('[正妹] 乃木坂46 一ノ瀬美空','https://www.ptt.cc/bbs/Beauty/M.1686293747.A.482.html')
'''

#下面是主程式
'''
while nm > 0:
    cookies = {'over18': '1'}
    rq_1 = requests.get(urL, myheaD, cookies=cookies).text
    souP = bf(rq_1, 'lxml')
    for i in souP.find_all('div', 'r-ent'):
        if i.find('div', 'date').text[3:] == daY:
            if '(本文已被刪除)' in i.find('div', 'title').text:
                print('(本文已被刪除)')
                print('~~' * 5)
            elif '違反板規' in i.find('div', 'title').text:
                print('(因違反板規，本文已被刪除)')
                print('~~' * 20)
            elif not ('(本文已被刪除)'or'違反板規') in i.find('div', 'title').text:
                a = i.find('div', 'title').text
                b = a.replace('\n', '')
                k = 'https://www.ptt.cc' + i.find('div', 'title').a['href']
                print(k)
                print(b)
                _copy(b, k)
                print('~~' * 5)
            else:
                print('error-2')
        elif i.find('div', 'date').text[3:] != daY:
            nm = nm - 1
            # print('-1')
        else:
            print('error-3')
    urL = str('https://www.ptt.cc' + souP.find('div', 'btn-group btn-group-paging').find_all('a', 'btn wide')[1]['href'])

'''   
    
