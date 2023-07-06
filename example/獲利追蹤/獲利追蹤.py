import twstock
import csv
import os
import pandas as pd
from pandas import Series, DataFrame

def now_csv():
    nu = input('代號')
    datA_1 = twstock.realtime.get(nu) 
    if datA_1['success']:
       csvfilE = open ('now_'+nu+'.csv','w',newline="",encoding="utf-8-sig")
       writE = csv.writer(csvfilE)
       writE.writerow(['股票代號','股票名稱','時間','現價(買)','現價(賣)'])
       a = datA_1['info']['code']
       b = datA_1['info']['fullname']
       c = datA_1['info']['time']
       d = datA_1['realtime']['best_bid_price'][0]
       e = datA_1['realtime']['best_ask_price'][0]
       #print(a,b,c,d,e)
       writE.writerow([a,b,c,d,e])
       print('資料儲存成功，並以'+'  '+'now_'+nu+'.csv'+'  '+'的形式存於'+os.getcwd())
    else:
        print('資料取得失敗')
	
'''
datA_1 = twstock.realtime.get("0050")

#print(datA_1)
print('timestamp',"~"*40)
print(datA_1['timestamp'])
print('info',"~"*40)
print(datA_1['info'])
print('realtime',"~"*40)
print(datA_1['realtime']) 
print('success',"~"*40)
print(datA_1['success']) 
print("~"*40)
'''

patH_1 = r'C:\my_github\mypytjon\example\獲利追蹤'
patH_2 = 'test'   
#dictFile = pd.read_excel(patH_1+'\\'+patH_2+'.xlsx')
#dictFile = pd.read_excel(patH_1+'\\'+'目標.xlsx')

#用cmd讀檔時要使用這行，記的(pip install xlrd & pip  install openpyxl)
#dictFile = pd.read_excel(patH_1+'\\'+'目標.xlsx',engine='openpyxl')


dictFile = pd.read_excel(patH_1+'\\'+patH_2+'.xlsx',engine='openpyxl')
#writE = xlsx.write(dictFile)
data_0 = ([0.9,-0.2],[0.5,0.2],[1,2])
df= DataFrame(data_0,columns=['A','B'],index=['one','two','three'])

writer = pd.ExcelWriter(patH_1+'\\'+patH_2+'.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

#print(dictFile)
'''
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
'''

patH_1 = r'C:\my_github\mypytjon\example\獲利追蹤'
patH_2 = 'test'
data_0 = ([0.9,-0.2],[0.5,0.2],[1,2])
df_0= DataFrame(data_0,columns=['A','B'],index=['one','two','three'])
writer = pd.ExcelWriter(patH_1+'\\'+patH_2+'.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

data_1 = ([9,-2],[5,2],[10,20])
df_1= DataFrame(data_1,columns=['A','B'],index=['one','two','three'])
writer = pd.ExcelWriter(patH_1+'\\'+patH_2+'.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name='Sheet2')
writer.save()

