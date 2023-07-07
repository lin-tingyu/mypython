import pandas as pd
import openpyxl
import twstock
from datetime import datetime#時間
import numpy as np# np.arange
patH_1 = r'C:\my_github\mypytjon\example\獲利追蹤'
patH_3 = '目標'

def _indvidual(nu):
    datA = twstock.realtime.get(nu)
    t = datA['info']['time']#2
    #t_1 = datA['info']['time'][5:10]
    n =datA['info']['name']#3
    datAPrice_1=float(datA["realtime"]["best_bid_price"][0])
    datAPrice_2=float(datA["realtime"]["best_ask_price"][0])
    datAPrice_3 = (datAPrice_1+datAPrice_2)/2 
    p =datAPrice_3 #4
    v = datA["realtime"]["accumulate_trade_volume"]#5
    time_now = datetime.now()
    now = time_now.strftime("%H:%M:%S")#1
    roW_1 = [now,t,n,p,v]
    return roW_1
    

dictFile = pd.read_excel(patH_1+'\\'+patH_3+'.xlsx',engine='openpyxl',dtype={'股票代號':str} )
roW_name = ["當前時間",'資料時間','股票名稱','現在價格','交易量']
#print(roW_name)
roW = []
for i in range(len(dictFile['股票代號'])):
    #print(dictFile['股票代號'][i])
    roW_1 = _indvidual(dictFile['股票代號'][i])
    roW = np.array(roW_1).reshape(1,5)
    data_0 = ()
    #df_0 = pd.DataFrame(data_0,columns=[roW[0]],index=roW_name)
    df_0 = pd.DataFrame(data_0,columns=roW_name,index=[roW_1[1][5:10]])
    data_1=roW
    #df_1 = pd.DataFrame(data_1,columns=[roW[0]], index=roW_name)
    df_1 = pd.DataFrame(data_1,columns=roW_name,index=[roW_1[1][5:10]])
    patH_2 = roW_1[1][:10]
    Sheet = roW_1[2]
    try:
        try:#如果有xlsx檔，也有Sheet
            book = openpyxl.load_workbook(patH_1 + '\\' + patH_2 + '.xlsx')
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




















