import requests
from bs4 import BeautifulSoup as bf
import pandas as pd
import openpyxl
import twstock
from datetime import datetime#時間
import numpy as np# np.arange

myHead={'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
patH_1 = r'C:\mypython\example\MOMO價格追蹤'#資料讀去路徑
patH_3 = '物品欄'#資料讀去路徑(資料夾名)

def _information_get():
    #dictFile = pd.read_excel(patH_1+'\\'+patH_3+'.xlsx',engine='openpyxl' )
    #urL =dictFile['URL'][i]
    #name = dictFile['商品'][i]
    urL = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10372280&seller=20190703150015290&osm=Ad09&utm_source=BD_015457&utm_medium=Google-SEM&scm_activity=202305020429t78po3gu&gclid=Cj0KCQjw756lBhDMARIsAEI0AgkKzf_28JK442SIDW88jIrLRpIrLK0_G4K7w-v_3WOnSubDuW7q_9QaAuwKEALw_wcB"
    rq_1 = requests.get(urL,headers=myHead).text
    souP_1 = bf(rq_1,'html5lib')
    souP_2 = souP_1.find('div','prdnoteArea jsCartFloat')
    pricE = []
    pricE_6 = []
    datA = []
    souP_3 = souP_2 .find('span').text
    #print(souP_3)#名子
    #促銷價格
    souP_5 = souP_2 .find('ul','prdPrice')
    for i in souP_5.find_all('li'):
        pricE.append(i.text.strip())
    #print(pricE)
   
    souP_4_1 = souP_2 .find('li').text.strip()
    souP_4 = souP_4_1.replace(u'\xa0',u'')
    #print(souP_4)#促銷時間
    #促銷價格   
    souP_6 = souP_2 .find('ul','relateMarketing gmclass')
    for i in souP_6.find_all('li'):
        #print(i.text.strip())
        a =i.text.strip()
        a_1 = a.replace(u'\xa0', u'')
        pricE_6.append(a_1)
    #print(type(pricE_6[0]))
    #print(pricE_6)
    souP_7 = souP_2.find('ul','ineventArea').span.text.strip()
    #print(souP_7)
    #print(noW_1)
    datA = [souP_3,pricE[0],pricE[1],souP_4,pricE_6[0],souP_7]
    #print(datA)
    return datA

#print(_information_get(0))
  
dictFile = pd.read_excel(patH_1+'\\'+patH_3+'.xlsx',engine='openpyxl' )

roW_name = ['目標品項','搜尋品項','市價','促銷價','促銷價時間','備註_1','備註_2']#columns編號
noW = datetime.now() 
noW_1 =noW.strftime("%Y-%m/%d")
#print(type(noW_1))
roW_1 = ['時間']#index編號
roW_2=_information_get()
roW_2.append(noW_1)


roW_2=_information_get()
roW_2.append(noW_1)
roW = np.array(roW_name).reshape(1,7)

data_0 = ()  
df_0 = pd.DataFrame(data_0,columns=roW,index=[noW_1])
data_1=np.array(roW_2).reshape(1,7)
df_1 = pd.DataFrame(data_1,columns=roW,index=[noW_1])
patH_2 = '價格追蹤'#資料儲存路徑(資料夾名)
Sheet = dictFile['商品'][0]#資料儲存路徑(sheet名)
#print(data_1)
#print(roW)


try:
    try:#如果有xlsx檔，也有Sheet
        book = openpyxl.load_workbook(patH_1 + '\\' + patH_2 + '.xlsx')#資料儲存路徑
        writer = pd.ExcelWriter(patH_1 + '\\' + patH_2 + '.xlsx', engine='openpyxl',mode="a", if_sheet_exists="overlay")
        writer.book = book
        sheet1 = writer.book[Sheet]
        start_row = sheet1.max_row 
        df_1.to_excel(writer, sheet_name=Sheet,startrow=start_row,index=True, header=True)
        writer.save()
    except:#如果有xlsx檔，沒有Sheet
        with pd.ExcelWriter(patH_1 + '\\' + patH_2 + '.xlsx', engine='openpyxl',mode="a", if_sheet_exists="overlay") as writer:
            df_0.to_excel(writer, sheet_name=Sheet)#不存在時會自動生成
            df_1.to_excel(writer, sheet_name=Sheet,index=True, header=True)
            writer.save()
except:#如果沒有xlsx檔
    with pd.ExcelWriter(patH_1 + '\\' + patH_2 + '.xlsx', engine='openpyxl',mode="w") as writer:
        df_0.to_excel(writer, sheet_name=Sheet)#不存在時會自動生成
        df_1.to_excel(writer, sheet_name=Sheet,index=True, header=True)
        writer.save()
writer.close()

'''
for i in range(len(dictFile['商品'])):
    roW_2=_information_get()
    roW_2.append(noW_1)
    roW = np.array(roW_name).reshape(1,7)
    data_0 = ()  
    df_0 = pd.DataFrame(data_0,columns=roW,index=roW_1)
    data_1=roW
    df_1 = pd.DataFrame(data_1,columns=roW,index=roW_1)
    patH_2 = '價格追蹤'#資料儲存路徑(資料夾名)
    Sheet = dictFile['商品'][i]#資料儲存路徑(sheet名)
    try:
        try:#如果有xlsx檔，也有Sheet
            book = openpyxl.load_workbook(patH_1 + '\\' + patH_2 + '.xlsx')#資料儲存路徑
            writer = pd.ExcelWriter(patH_1 + '\\' + patH_2 + '.xlsx', engine='openpyxl',mode="a", if_sheet_exists="overlay")
            writer.book = book
            sheet1 = writer.book[Sheet]
            start_row = sheet1.max_row 
            df_1.to_excel(writer, sheet_name=Sheet,startrow=start_row,index=True, header=True)
            writer.save()
        except:#如果有xlsx檔，沒有Sheet
            with pd.ExcelWriter(patH_1 + '\\' + patH_2 + '.xlsx', engine='openpyxl',mode="a", if_sheet_exists="overlay") as writer:
                df_0.to_excel(writer, sheet_name=Sheet)#不存在時會自動生成
                df_1.to_excel(writer, sheet_name=Sheet,index=True, header=True)
                writer.save()
    except:#如果沒有xlsx檔
        with pd.ExcelWriter(patH_1 + '\\' + patH_2 + '.xlsx', engine='openpyxl',mode="w") as writer:
            df_0.to_excel(writer, sheet_name=Sheet)#不存在時會自動生成
            df_1.to_excel(writer, sheet_name=Sheet,index=True, header=True)
            writer.save()
writer.close()
'''


