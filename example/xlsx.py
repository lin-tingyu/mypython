import pandas as pd
import openpyxl
import twstock
from datetime import datetime#時間
import numpy as np# np.arange
patH_1 = r''#資料讀去路徑
patH_3 = ''#資料讀去路徑(資料夾名)

   

dictFile = pd.read_excel(patH_1+'\\'+patH_3+'.xlsx',engine='openpyxl' )
roW_name = ['710','852','741','741','741']#columns編號
roW_1 = ['123','456']#index編號
roW =[]#資料內容
for i in range():
    roW = np.array(roW_name).reshape(1,5)
    data_0 = ()
    df_0 = pd.DataFrame(data_0,columns=roW,index=[roW_1[1][5:10]])
    data_1=roW
    df_1 = pd.DataFrame(data_1,columns=roW,index=[roW_1[1][5:10]])
    patH_2 = ''#資料儲存路徑(資料夾名)
    Sheet = ''#資料儲存路徑(sheet名)
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




















