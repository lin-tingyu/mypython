'''
[IFTTT]+[LINE]+[twstock]--專題製作示範程式
'''
import requests
import twstock
import time
from datetime import datetime#時間

evenT="stock"
myCode="b3SN1RVtk9SO39mHEoMttO"
valuE1="元大台灣50"
iD="0050"
lowPrice=127.7
highPrice=128

while True:  #在IPython console按右鍵選擇[Quit]可以中斷程式
    realData=twstock.realtime.get(iD)
    if realData["success"]:
        realPrice_1=float(realData["realtime"]["best_bid_price"][0])
        realPrice_2=float(realData["realtime"]["best_ask_price"][0])
        realPrice_3 = (realPrice_1+realPrice_2)/2
        valuE3=str(realPrice_3)
        if realPrice_3 >= highPrice:
            valuE2="越過"+str(highPrice)
            urL="https://maker.ifttt.com/trigger/"+evenT+"/with/key/"+myCode+"?value1="+valuE1+"&value2="+valuE2+"&value3="+valuE3
            replY=requests.get(urL)
            print(replY)
            #break
        elif realPrice_3 <= lowPrice:
            valuE2="跌破"+str(lowPrice)
            urL="https://maker.ifttt.com/trigger/"+evenT+"/with/key/"+myCode+"?value1="+valuE1+"&value2="+valuE2+"&value3="+valuE3
            replY=requests.get(urL)
            print(replY)
            #break
        else:    
            print("nothing happen.....",end='')
            print("  ||  當前價格:",realPrice_3)
            time_now = datetime.now()
            now = time_now.strftime("%Y-%m/%d %H:%M:%S")
            print("當前時間:", now)
            print("資料時間:",realData['info']['time'])
            print('~~'*20)

            
    else:
        print("Error: "+realData["rtmessage"])
    time.sleep(60)
    

