import requests#json爬蟲
import json#json爬蟲，將檔案存成json檔
from bs4 import BeautifulSoup#bs4爬蟲
import csv#將檔案存成csv檔

myHead={'usere-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
'''
#自由時報
urL="https://news.ltn.com.tw/list/breakingnews"
rq_1=requests.get(urL)
bs_1= BeautifulSoup(rq_1.text,'lxml')
'''


#聯合電子報
urL ="https://paper.udn.com/papers.php?pname=PID0001"
rq_1=requests.get(urL)
rq_1.encoding='utf-8'
bs_1= BeautifulSoup(rq_1.text,'lxml')


#print(rq_1.text)
#rq_1.json()

#取得標題
print(bs_1.title.getText())

'''
#自由時報
soup_1_f1=bs_1.find('ul','list')
for i in soup_1_f1.find_all("li"):
    for j in i.find_all("a"):
        print(j.text.strip())
#加strip，可以去除除空白
'''

'''
#聯合電子報
for i in bs_1.find_all('div','history_list'):
    for j in i.find_all('li','subject'):
        key=j.text.strip()
        value_1=j.a['href']
    for j in i.find_all('li','date'):
        value_2=j.text
        dict[key]=[value_1,value_2]
  
'''

newS = {}

#聯合電子報
for i in bs_1.find_all('div','history_list'):
    for j in i.find_all('li','subject'):
        key=j.text.strip()
        value_1=j.a['href']
    for j in i.find_all('li','date'):
        value_2=j.text
        newS[key]=[value_1,value_2]
       

print(newS)


with open('ltnnews.json',"w",encoding='utf-8') as filE:
    json.dump(newS,filE,ensure_ascii=False,indent=4)
   

with open('ltnnews.json',"r",encoding='utf-8') as filE:
    ltnNews=json.load(filE)
  


csv_filE= open('news_1.csv','w',newline="",encoding="utf-8-sig")
writeR=csv.writer(csv_filE)
writeR.writerow(["時間","標題","超連結"])



#聯合電子報
for i in bs_1.find_all('div','history_list'):
    try:
        for j in i.find_all('li','subject'):
            titlE=j.text.strip()
            linK=j.a['href']
            #writeR.writerow((titlE,linK))
        for j in i.find_all('li','date'):
            timE=j.text
            writeR.writerow((timE,titlE,linK))
    except:
        continue

csv_filE.close()











