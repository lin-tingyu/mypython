import requests
from bs4 import BeautifulSoup as bf
import pandas as pd
import openpyxl
from datetime import datetime#時間
import numpy as np# np.arange
import os
import random

myHead={'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
patH_1 =os.getcwd()#資料讀去路徑
patH_3 = '物品欄'#資料讀去路徑(資料夾名)



def _information_get(urL):
    #dictFile = pd.read_excel(patH_1+'\\'+patH_3+'.xlsx',engine='openpyxl' )
    #urL =dictFile['URL'][i]
    #name = dictFile['商品'][i]
    #urL = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10372280&seller=20190703150015290&osm=Ad09&utm_source=BD_015457&utm_medium=Google-SEM&scm_activity=202305020429t78po3gu&gclid=Cj0KCQjw756lBhDMARIsAEI0AgkKzf_28JK442SIDW88jIrLRpIrLK0_G4K7w-v_3WOnSubDuW7q_9QaAuwKEALw_wcB"
    rq_1 = requests.get(urL,headers=myHead).text
    souP_1 = bf(rq_1,'html5lib')
    souP_2 = souP_1.find('div','prdnoteArea jsCartFloat')
    pricE = []
    datA = []
    #名子
    souP_3 = souP_2 .find('span').text
    #促銷價格
    souP_5 = souP_2 .find('ul','prdPrice')
    for i in souP_5.find_all('li'):
        pricE.append(i.text.strip())

    #print(noW_1)
    datA = [souP_3,pricE[0],pricE[1]]
    #時間
    noW = datetime.now() 
    noW_1 =noW.strftime("%Y-%m/%d")
    roW_1 = ['時間']#index編號
    datA.append(noW_1)
    return datA

def _save_xlsx(patH_2,df_0,df_1): 
    Sheet=random.randrange(2,1000,1)
    try:
        try:#如果有xlsx檔，也有Sheet
            book = openpyxl.load_workbook(patH_1 + '\\' + patH_2 + '.xlsx')#資料儲存路徑
            writer = pd.ExcelWriter(patH_1 + '\\' + patH_2 + '.xlsx', engine='openpyxl',mode="a", if_sheet_exists="overlay")
            book =writer.book
            sheet1 = writer.book[Sheet]
            start_row = sheet1.max_row 
            df_1.to_excel(writer, sheet_name=Sheet,startrow=start_row,index=True, header=False)
            writer.close()
        except:#如果有xlsx檔，沒有Sheet
            with pd.ExcelWriter(patH_1 + '\\' + patH_2 + '.xlsx', engine='openpyxl',mode="a", if_sheet_exists="overlay") as writer:
                df_0.to_excel(writer, sheet_name=Sheet)#不存在時會自動生成
                df_1.to_excel(writer, sheet_name=Sheet,index=True, header=True)
                writer.close()
    except:#如果沒有xlsx檔
        with pd.ExcelWriter(patH_1 + '\\' + patH_2 + '.xlsx', engine='openpyxl',mode="w") as writer:
            df_0.to_excel(writer, sheet_name=Sheet)#不存在時會自動生成
            df_1.to_excel(writer, sheet_name=Sheet,index=True, header=True)
            writer.close()
    print('資料已儲存，位置於:',patH_1,'中的','\n',patH_2+'.xlsx')

  

def _read_Target():
    dictFile = pd.read_excel(patH_1+'\\'+patH_3+'.xlsx',engine='openpyxl' )#物品欄
    for i in range(len(dictFile['商品'])):
        roW_2 = _information_get(dictFile['URL'][i])
        data_1=np.array(roW_2).reshape(1,4)#內容轉

    #表頭資料
    roW_name = ['搜尋品項','市價','促銷價','時間']#columns編號
    roW = roW_name#表頭不轉

    #整理成DataFrame
    df_1 = pd.DataFrame(data_1,columns=roW,index=[roW_2[-1]])
    #Sheet = dictFile['商品'][0]#資料儲存路徑(sheet名)
    return df_1

def _title_only():
    noW = datetime.now() 
    noW_1 =noW.strftime("%Y-%m/%d")
    data_0 = ()  
    roW_name = ['搜尋品項','市價','促銷價','時間']#columns編號
    roW = roW_name#表頭不轉
    df_0 = pd.DataFrame(data_0,columns=roW,index=[noW_1])
    return df_0

def _Sheet():
    dictFile = pd.read_excel(patH_1+'\\'+patH_3+'.xlsx',engine='openpyxl' )#物品欄
    for i in range(len(dictFile['商品'])):
        Sheet ='葉黃素'
 
#print(df_0)
#print(df_1)
patH_2 = '價格追蹤_1'#資料儲存路徑(資料夾名)
_save_xlsx(patH_2,_title_only(),_read_Target())
#a = input('123')
#print(_read_Target())


#dictFile = pd.read_excel(patH_1+'\\'+patH_3+'.xlsx',engine='openpyxl' )#物品欄
    #print(len(dictFile['商品']))
'''  
for i in range(len(dictFile['商品'])):
    #print(i)
    #print(dictFile['URL'][i])
    roW_2 = _information_get(dictFile['URL'][i])
    data_1=np.array(roW_2).reshape(1,7)#內容轉
    #表頭資料
    roW_name = ['目標品項','搜尋品項','市價','促銷價','促銷價時間','備註_1','備註_2']#columns編號
    roW = roW_name#表頭不轉
    #整理成DataFrame
    df_1 = pd.DataFrame(data_1,columns=roW,index=[roW_2[-1]])
'''

#個別測試
# print(dictFile['URL'][1])
# roW_2 = _information_get('https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10501910')
# print(roW_2)

'''
data_1=np.array(roW_2).reshape(1,7)#內容轉
#表頭資料
roW_name = ['目標品項','搜尋品項','市價','促銷價','促銷價時間','備註_1','備註_2']#columns編號
roW = roW_name#表頭不轉
#整理成DataFrame
df_1 = pd.DataFrame(data_1,columns=roW,index=[roW_2[-1]])
'''

