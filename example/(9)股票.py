import twstock#抓取台灣股票資料
#(pip install twstock-->import twstock-->twstock.__update_codes())
#twstock.__update_codes()(代碼跟新)
import csv
import os

def _now_csv():
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
    csvfilE.close()

def _month_csv():
    nu = input('代號')
    stock = twstock.Stock(nu)
    y = input('年')
    m = input('月')
    datA = stock.fetch(int(y),int(m))
    
    csvfilE = open(nu+'+'+y+m+'.csv','w',newline="",encoding="utf-8-sig") 
    writE = csv.writer(csvfilE)
    writE.writerow(['日期','price','kind'])

    for i in range(len(datA)): 
        d = str(datA[i][0])
        dd = d.split(' ')[0]
        
        o = str(datA[i][3])
        h = str(datA[i][4])
        l = str(datA[i][5])
        c = str(datA[i][6])
        print([dd,o,h,l,c])
        writE.writerow([dd,o,'open'])
        writE.writerow([dd,h,'high'])
        writE.writerow([dd,l,'low'])
        writE.writerow([dd,c,'close'])
    print('資料儲存成功，並以'+'  '+nu+'+'+y+m+'.csv'+'  '+'的形式存於'+os.getcwd())
    csvfilE.close()
     
def _now_print():
    nu = input('代號')
    datA_1 = twstock.realtime.get(nu) 
    if datA_1['success']:
        print(datA_1["realtime"]["best_bid_price"][0])
        print(datA_1["realtime"]["best_ask_price"][0])
    else:
        print('資料取得失敗')


#now_csv()
#_month_csv()
#_now_print()

datA_1 = twstock.realtime.get('00632R')
print(datA_1['success'])














