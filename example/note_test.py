import requests
from bs4 import BeautifulSoup as bf

myHead={'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

#yahoo 新聞

'''
urL = "https://tw.news.yahoo.com/"
rq_1 = requests.get(urL).text
souP_1 = bf(rq_1,'lxml')
#print(souP_1.title.getText())

for i in souP_1.find_all('li','Pos(r) Lh(1.5) H(24px) Mb(8px)'):
	souP_2 = i.find('a')
	souP_3 = souP_2['href']
	print(souP_2.text)
	print(souP_3)
	print('~'*20)

'''
#feebee 比價

'''
urL = "https://feebee.com.tw/s/?q=%E6%B3%A1%E9%BA%B5"
rq_1 = requests.get(urL,headers=myHead).text
souP_1 = bf(rq_1,'html5lib')
souP_2 = souP_1.find('ol')

for i in souP_2.find_all('li'):
	try:
		souP_3 = i.find('span','pure-u items_container')
		souP_4 = souP_3.a.h3.text.strip()
		#souP_5 = i.find('span','price ellipsis xlarge').text.strip()
		#souP_6 = i.find('div','price-info')
		#souP_7 = souP_6.find('a','campaign_link campaign_link_price')['href']
		print(souP_4)
		print(type(souP_4))
		#print('新台幣:',souP_5)
		#print(souP_7)
		print('~'*20)
	except:
		continue


'''

#feebee用select
'''
urL = "https://feebee.com.tw/s/?q=%E6%B3%A1%E9%BA%B5"
rq_1 = requests.get(urL,headers=myHead).text
souP_1 = bf(rq_1,'html5lib')
souP_2 = souP_1.select_one('ol')
#print(souP_2)


for i in souP_2.select("li"):
	try:
		souP_3 = i.select('span.pure-u.items_container > a > h3')
		#~~~~~~~~
		souP_5 = i.select('span.pure-u.items_container > div.price-info > a> span')
		#souP_6 = i.select_one('span.pure-u.items_container > div.shop_container.ellipsis ')
		#~~~~~~~
		souP_6 = i.find('div','price-info')
		souP_7 = souP_6.find('a','campaign_link campaign_link_price')['href']
		#~~~~~~~
		if souP_3==[]:
			continue
		else:
			print(souP_3)
			print(souP_5_1)
			print(souP_7)
			print('~'*40)
	except:
		#print('~'*40)
		continue
'''






