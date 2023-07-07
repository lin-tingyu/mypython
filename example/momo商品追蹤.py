import requests
from bs4 import BeautifulSoup as bf

myHead={'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}


urL = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10372280&seller=20190703150015290&osm=Ad09&utm_source=BD_015457&utm_medium=Google-SEM&scm_activity=202305020429t78po3gu&gclid=Cj0KCQjw756lBhDMARIsAEI0AgkKzf_28JK442SIDW88jIrLRpIrLK0_G4K7w-v_3WOnSubDuW7q_9QaAuwKEALw_wcB"
rq_1 = requests.get(urL,headers=myHead).text
souP_1 = bf(rq_1,'html5lib')
souP_2 = souP_1.find('div','prdnoteArea jsCartFloat')

souP_3 = souP_2 .find('span').text
souP_4 = souP_2 .find('li').text.strip()

#促銷價格
souP_5 = souP_2 .find('ul','prdPrice')
#for i in souP_5.find_all('li'):
    #print(i.text.strip())

#促銷價格   
souP_6 = souP_2 .find('ul','relateMarketing gmclass')
for i in souP_6.find_all('li'):
    print(i.text.strip())



