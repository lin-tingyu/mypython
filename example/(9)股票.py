import twstock#抓取台灣股票資料
#(pip install twstock-->import twstock-->twstock.__update_codes())
#twstock.__update_codes()(代碼跟新)
import csv


nu = input('代號')
stock = twstock.Stock(nu)
y = input('年')
m = input('月')


datA = stock.fetch(int(y),int(m))
#datA_1 = stock.realtime.get('2330')#抓及時股價


csvfilE = open(nu+'.csv','w',newline="",encoding="utf-8-sig") 
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

csvfilE.close()


























