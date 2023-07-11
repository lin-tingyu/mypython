import numpy as np# np.arange
from pandas import Series, DataFrame
import pandas as pd
import time
from datetime import datetime#時間
from datetime import timedelta#時間(幾天候)
import pandas as pd #匯入excell
import random # random
pd.core.common.is_list_like = pd.api.types.is_list_like#網路抓資料
from pandas_datareader import data, wb#網路抓資料
import pandas_datareader.data as web#網路抓資料
from pytrends.request import TrendReq#下載 google trend
import pandas_datareader as pdr#從API抓資料(例:tiingo)
#其他API資料: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html
from scipy.stats import norm#統計 pdf
import matplotlib.pyplot as plt#畫圖(1)
from pylab import mpl#可以讓matplotlib.pyplot顯示中文
import seaborn as sns;#畫圖(2)
#scatterplot輔助繪製圖表的工具，還是需要matplotlib.pyplot才能運行
#詳細可去官網https://seaborn.pydata.org/examples/index.html查看
#須安裝(pip install seeborn)
import plotly.express as px#繪圖工具
import statsmodels#statsmodels.stats.weightstats.ttest_ind
import statsmodels.formula.api as smf#ols
import statsmodels.api as sm#ols & sm.Logit
import pickle
import pyreadstat#讀dta檔 pyreadstat.read_dta
import csv#將檔案存成csv檔
from PIL import Image#光學辨識外掛(要先安裝:pip install Pillow)
#還需安裝此套件:https://digi.bib.uni-mannheim.de/tesseract/
import pytesseract#光學辨識外掛(要先安裝:pip install pytesseract)
import nltk#識別文字，以英文為主(pip install nltk) 
import jieba#要識別中文要將上這個(pip install jieba)
import linearmodels#pip install linearmodels
import requests#爬蟲，網路通訊協定資料庫
#如果urllib3有問題(pip install urllib3==1.26.6)
from bs4 import BeautifulSoup#爬蟲，解析html資料庫
import json#json爬蟲，將檔案存成json檔
import twstock#抓取台灣股票資料
#(pip install twstock-->import twstock-->twstock.__update_codes())
#twstock.__update_codes()(代碼跟新)



















###注意事項####檔案名稱(***.py)，不能和安裝包名稱相同
#系統環境設定
'''
設定路徑：
1.開啟cmd
2.寫入set path：(安裝完的資料夾位置);%path%
範例：
	set path：C:\Users\USER\AppData\Local\Programs\Python\Python310;%path%
3.寫入python -V 來確認是否設定完畢
4.寫入set path =(安裝完的資料夾位置)\Scripts;%path%
範例：
	set path：C:\Users\USER\AppData\Local\Programs\Python\Python310\Scripts;%path%
5.寫入 pip list 來確認是否設定完畢
'''
#python 函式庫功能查詢
#https://docs.python.org/zh-tw/3.10/index.html
#儲存資料之基本元素
a_1 = (1,2)#此為tuple(元組)
a_2 = [1,2]#此為list(串列)
a_3 = {1,2}#此為set(集合)
a_4 = {'a':[1,2],'b':[4,5]}#此為dict(字典)
a_5 = np.array(a)#此為array(陣列)
a_6 = DataFrame(a_1)#此為DataFrame(數據幀)
a_7 = #此為matrix(矩陣)
a_8 = #此為serise(序列)
b = list(a_1)#改list
c = tuple(b)#改tuple
print(help(a))#查詢使用方式
#基本元素---tuple()元組，內容&個數不能變動
tuple_1 = (1,2,3)
tuple_2 = ('a','b','c')
print(max(tuple_1))
print(tuple(enumerate(tuple_2)))
tuple_3=list(zip(tuple_1,tuple_2))#合起來，一定要變list 
print(tuple_3)
tuple_1_1,tuple_2_1 =zip(*tuple_3)#拆回來
#基本元素---list[]串列
a=[2,3,4,5];
a.append(6) #增加一個新的元素
a.insert(0,1)#增加一個新的元素
print(len(a))#顯示行列數:只有一個為度時不能顯示
game1,game2,game3,game4,game5,game6 = a#赴值
print(a[0:6:3],a[:3],a[4:],a[-1],sep="~~")#呼叫
b=[7]
del a[0]#減少一個新的元素
a+=b#增加一個新的元素
#基本元素---print & input

list_0 = (1, 2)
list_1 = [1,2,3,'a']
list_1.append(list_0)#可以增加list&tuple
print(list_0 in list_1)
list_1.remove(list_0)#可以刪list&tuple
list_2 = ['b','c']
list_1.extend(list_2)
list_3 = [x**2 for x in list_1 if type(x)==int]
    #a.b.c不見，只有一維度時才能用for
english =['a','b','c']
for ii in range(0,len(english),1):
    a=english[ii]
    list_1.remove(a)#刪除特定字元，一次只能刪一個
list_4=list_1#deep copy
list_5=list_1[:]#shallo copy
print(id(list_4))
print(id(list_5))
popped_list=list_1.pop(2)#刪除特定"位置"字元
str='012abcd'
print(list(a))#可將字串拆開
#基本元素---array(陣列)
data_0 = ([0.9,-0.2,-0.8],[0.5,0.2,0.9],[1,2,3])
data_1 = [(1,2,3),(2,3,4),(1,2,3)]
data_00 = np.array(data_0)#將tuple轉成array，每一個小list裡的資料型態與數量必須是相同的!
data_11 = np.array(data_1)#將list轉成array，每一個小tuple裡的資料型態與數量必須是相同的!
len(data_00)
data_00.size
data_00.shape
data_00.T
data_2 = np.column_stack((data_00,data_11))#橫向合併
data_3 = np.row_stack((data_00,data_11))#直向合併
    #tuple()&list[]&array都可以使用，set{}不行
#print的使用
score = 90
name = 'ray'
count = 1
a=[2,3,4,5]
print("加總=%2.1f\n最大%2d\n最小%2d"%(sum(a),max(a),min(a)))#舊式表示法
print("%-10s你第%-10d次成績是%-10.1f分"%(name,count,score))#舊式表示法
print('姓名：'+'\n'+chr(26519)+chr(24237)+chr(23431))
print('{0:5.3f},{0:^10d},{2:.2%}'.format(5,10,15))#新式表示法
year = input('輸入您的年齡')#以字串儲存
year = eval(input('輸入您的年齡'))#自動分別int或float，以數字形式儲存
print(r'\n')#跳脫字元
print(ord("宇"))
print('123',end='')#不換行
#Tuples()和list[]共用
test=['a','b']
max
x = enumerate(test)
#基本元素---range
r1 = np.arange(0,10,1)
r2 = np.arange(0,10)
r3 = np.arange(10)
#矩陣---抓資料
data_0 = ([0.9,-0.2,-0.8],[0.5,0.2,0.9],[1,2,3])
data_1 = [(1,2,3),(2,3,4),(1,2,3)]
data_00 = np.array(data_0)#轉成矩陣一個 array 裡的資料型態與數量必須是相同的!
data_11 = np.array(data_1)
data_00[0][0]
data_1=data_00[:,1:2]#只有一列
data_1[0]=0#data_00也會改變
data_00>0 # 看看 data 哪裡大於 0
names = np.array(['Alice','Bob','Charles'])
data_2 = data_1[names=='Bob'] #names=='Bob'等價[2] names跟data要同為度
data_3 = data_00[(names=='Alice') | (names=='Charles')]# | 可分行抓資料  
    #“|” and “&” 分別代表 “且” 和 “或” 的邏輯符號
#矩陣---加減乘除
#series 
a = Series([4,7,-5,3], index=['a','b','c','d']) 
#字典型態---Numpy來模擬Series
#無法輸入重複的'鍵'
dic_1 ={'a':[4,5,6],'b':[7,8,9]}
dic_1['c']=[-5,-4,-3]#增加元素
dic_2=dic_1.copy()#將x的內容複製到y(shallo copy)
print(dic_1.get('c')[0])#取值(方法一)
print(dic_1['c'][0])#取值(方法二)
for i,j in dic_1.items():
    print('鍵(keys):',i,' | ','值(values):',j)
print('x的位置',id(x),'\ny的位置',id(y))#x&y為不同東西
a = ['a','b','c','d'] 
dic_4 = dict.fromkeys(a)#，將字串轉成字典，只能輸入於'鍵'
dic_5 = {'a':4, 'b':7,'c':-5,'d':3}
DF_1 = DataFrame(dic_1)#將字典轉成dataframe，記得大寫 (dic_1在131行)
DF_1.index=(['one','two','three'])#改index 
#DataFrame(矩陣轉DataFrame)
data_0 = ([0.9,-0.2],[0.5,0.2],[1,2])
DF_2 = DataFrame(data_0,columns=['A','B'],index=['one','two','three'])
    # 如果在 columns 給予未定義的 column name，pandas 會自動填滿 NaN
DF_2.loc[1:2].T
DF_2.A#只能叫出columns'Alice'
DF_2.loc['one']#叫出loc'one'
#DataFrame---提取資料長寬
print(len(DF_2['A']))#DF_2中'A'行的長度
print(DF_2['B'].count())#DF_2中'B'行的長度
print(DF_2.shape[1])#DF_2的寬度
print(DF_2.shape[0])#DF_2的長度
#DataFrame---提取資料標頭與索引
print(DF_2.columns)#標頭
print(DF_2.index)#索引
#DataFrame---搜尋
print(DF_2[DF_2.A ==0.9])
print(DF_2[(DF_2.A > 0.9) | (DF_2.A <0.9)])
#DataFrame---合併
DF_3 = DF_2.join(DF_1)#橫向
DF_2.index=(['one_1','two_2','three_3'])#合併時注意index名子，此時資料還在
DF_2.columns=['a','b']#合併時注意columns名子，此時資料還在
DF_4=pd.concat([DF_2,DF_1],axis = 0)#1=橫向 0=綜向
#DataFrame---加行列(非改名，資料會不見)
DF_2.reindex(['two','three','four'])#one的row&資料不見了
#DataFrame---刪資料
DF_4.drop('one',axis = 0)#1=橫向 0=綜向
#DataFrame---整理(groupby)
dict_obj = {'key1' : ['a', 'b', 'a', 'b', 
                      'a', 'b', 'a', 'a'],
            'key2' : ['one', 'one', 'two', 'three',
                      'two', 'two', 'one', 'three'],
            'data1': np.random.randn(8),
            'data2': np.random.randn(8)}
df_obj = pd.DataFrame(dict_obj)

grouped1 = df_obj.groupby('key1')
print(grouped1.describe())
#sum() max() min() mean() size() count() describe() prod()非na值之積
print(df_obj.groupby('key1').agg('mean', 'std'))
grouped2 = df_obj.groupby(['key2', 'key1'])
print(grouped2.mean())
print(grouped2.mean().unstack())
for group_name, group_data in grouped1:
    print(group_name)
    print(group_data)
     #https://cloud.tencent.com/developer/article/1193823
#Dataframe---運算
#Dataframe----敘述統計與排序
#set(集合)
'''
1.無法輸入同樣的東西
2.無法輸入list(因為它可以自行擴張)
str="012abcd"
print(set(a))#可將字串拆開，未排序
print(frozenset(a))#為不可便集合，如同tuple
add :新增
copy :是shallow copy
difference :a~(b)，留下a獨有的
difference_update :a~(b)刪除a中重複的，b會完整保留
intersection :重複的(和symmetric_difference相反)
isdisjoint :有無交集，T表示沒有
issubset :a~(b)(a是不是b的子集合)T表示b大
issuperset :a~(b)(a是不是b的超集合)T表示a大
discard :刪除指定物件
pop :隨機刪除物件
symmetric_difference:a~(b)，將ab獨有的都留下(和intersection'相反) 
clear:
union:兩邊有的都加起來
'''
#函數
#範例一:基本運用
def b(x,c,p):
    print(x,' ',c,'',end='')
    for i in range(3):
        print('第',i+1,'個數為',p[i],'    ',end='')
    print('')

list=[[1,2,3],[4,5,6],[7,8,9]]
s = ['A','B','C']
d = ['z','x','c']
for i in range(0,3):
    b(s[i],d[i],list[i])
#範例二:遞迴(算出N!)
def c(n):
    if n==1:
        return 1
    elif n!=1:
        return n*c(n-1)
    else: 
        print('error') 
     
n=int(input('請輸入數值n='))
print(c(n))
#範例三:計算機
def computer(a=1,m,b=1):
    if m=='+':
        return a+b
    elif m=='-':
        return a-b
    elif m=='*':
        return a*b
    elif m=='/':
        return a/b
    else:
        return 'error'
    
while(True):
    a = input('請輸入第一個計算值')
    if a=='q':
        break
    elif a!='q':
        a=int(a)
    else:
        print('error')
    m = input('請輸入運算子')
    b = int(input('請輸入第二個計算值'))
    print(computer(a,m,b))
#iter(疊代)
tuple_1 = (1,2,3)
iter_1= iter(tuple_1)
print(next(iter_1))
print(next(iter_1))
#lambda(匿名函數)
def total_price(people):
    return lambda price ,tip : (people *price)+tip
today =total_price(5)
print(today(50,10))
#CSV
a =['a','b','c']
b =[[1,2,3],
    [4,5,6],
    [7,8,9]]
file_1=open('檔案名','wt+',newline="",encoding='utf-8-sig')
#unix-link跳行"\n"及回歸行首"\r"兩者分開，windows是"\n\r"兩者混在一起，wt+是python要自動解決前述問題的方法，平常就用w+即可
writeR=csv.writer(file_1)
writeR.writerow(a)#寫入一維的資料
writeR.writerow(b)#寫入一維的資料

file_1.close()#切記，最後一定要加這行
    
#字串轉化為Python的time
    #時間處理:https://kknews.cc/zh-tw/finance/yz354vg.html
a = '89-MAR-2'#兩種資料類型不同
a_0 = datetime.strptime(a,'%y-%b-%d')
a_1 = datetime(2011,1,2)#和b不同格式
b_0 = pd.to_datetime(a, format='%y-%b-%d')
b_1 = pd.to_datetime('2011-1-2')#和a不同格式
    #時間代號: https://www.delftstack.com/zh-tw/howto/python/how-to-convert-string-to-datetime/
#time(import time)
print(time.strftime('%W'))#本日是今年的第幾周
#Time Series data
print(f'當前時間：{datetime.now()}')#當前時間 
time_now = datetime.now()#當前時間(now) 
now = time_now.strftime("%Y - %m/%d - %H:%M:%S")#當前時間(now) 
print("當前時間", now)#當前時間(now)  
datetime(2019,1,10)+timedelta(50)
    #20190110之後的50天，代號；?timedelta
ts = DataFrame(np.random.randn(1000),
               index=pd.date_range('2001-01-01',periods=1000,freq='MS'))
ts1 = ts['2001-01-01':'2001-04-01']
ts2 = ts['2001-02-01':'2001-05-01']
ts3=ts2.add(ts1,fill_value=0)#補完再加
ts3.plot()
#Panel Data---匯入資料 https://blog.csdn.net/caibaoH/article/details/78335094
loc = 'C:\\Users\\Lin ting yu\\Desktop'
filename = '123.xls'
#Panel Data---excell
#https://vimsky.com/zh-tw/examples/usage/python-pandas.ExcelWriter.html
path= r'C:/Users/Lin ting yu/Desktop/論文/數據'
dictFile = pd.read_excel(path+'.xlsx',engine='openpyxl',dtype={'股票代號':str})#指定讀取格式為str
df = pd.read_excel(path+'/月資料.xls',skiprows=[0,2,242])#xls 
df2 = pd.read_csv(path+'/金鐘獎 101_106.csv', header =None, names=('ABCD'))
    #sheet_name=0 第一個col不是名子
    #index_col =0 第一個roe不是名子
    #skiprows=[0,1,2] 消除第幾行
    #na_values = missing_values 遺漏值定義

#Panel Data---missing values
df.isnull().sum()# 計算每一個 column 有 missing values/data 的個數
df.replace(0,np.nan)#將 0 替換成 NaN
df.dropna(axis =1, how = 'all')
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
    #將 missing values/data 的整排觀察值全部丟棄
    #axis= 1為 columns，0為默認
    #any為只要有一個就丟(默認)，all為全部都是 missing values才丟
    #inplace=True 存回去
random.seed(30)#需要import random
dff = pd.DataFrame(np.random.randn(10, 3), columns=list('ABC'))
dff['A_1']=dff['A']
dff.iloc[3:5, 0] = np.nan
dff['A_f'] = dff['A'].fillna(method='ffill')
dff['A_mean'] = dff['A'].fillna(dff['A'].mean())
    #ffill較高值  bfill較低值，fillna(0)已0為值
dff[['A_f','A_mean','A_1']].plot() 
    # DataFrame 後面可以直接以 plot() 作為畫圖的最基本用法
#Panel Data---missing values(進階)WEEK4
from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"] #(from pylab import mpl) 
mpl.rcParams["axes.unicode_minus"] = False#(from pylab import mpl) 
#創圖紙(方法一)(圖紙子圖創完再丟資料)
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax4.plot(np.random.randn(30),'k--')
fig3,a = plt.subplots(2,2)
a[1,1].plot(np.random.randn(30).cumsum(),'k--')
    # 在 ax1 這個物件底下畫圖, k: 黑色, -- 虛線
#創圖紙(方法二)(將資料劃在圖紙子圖)(比較美)
df = DataFrame(np.random.randn(10,1),index=np.arange(0,100,10))    
fig,axes = plt.subplots(2,1)#只有一張:fig2, axs = plt.subplots(1)
df.plot(kind='hist',bins=30,grid=True,ax=axes[0])
    #grid:格子
#創圖紙(方法一+迴圈)(把迴圈跑出的資料劃出)
fig2,axes = plt.subplots(2,3,sharex=True,sharey=True)
    # 創建一個 fig3 物件 (組圖), 透過 plt.subplots, sharex: 橫坐標軸統一與否
    # axes 是一個 ndarray 用來儲存子圖物件的
for ii in range(2):
    for jj in range(3):
        axes[ii,jj].plot(np.random.randn(30).cumsum(),'k--')
#圖紙調整
fig.subplots_adjust(left=0,right=1.8,bottom=-1.2,wspace=00.1,hspace=1)
    #left:左界<右 wspace:圖與圖的左右距離 wspace:圖與圖的上下距離
fig.suptitle('Big title') # 設置整個圖的 title

#點線圖
ax1 = fig.add_subplot(2,2,1)
ax1.plot(np.random.randn(30).cumsum(),'k--',label='series 1')
    # 在 ax1 這個物件底下畫圖, k: 黑色, -- 虛線
# 直方圖
ax2 = fig.add_subplot(2,2,2)
ax2.hist(np.random.randn(100),bins=15,color='red')
    # bins: 切多少區塊, 詳細設定可以看 ?plt.hist
#散佈圖
ax3 = fig.add_subplot(2,2,3)    
ax3.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
ax4 = fig.add_subplot(2,2,4) 
path = r'C:/Users/Lin ting yu/Desktop/Python(2)'
team = pd.read_csv(path+'/Teams.csv',header = 0)
mlb2018 = team[team['yearID'] == 2018]
#散佈圖(不能再子圖)(import seaborn as sns; sns.set())
sns.scatterplot(x='teamID', y='ERA', hue='lgID',data=mlb2018)
plt.xticks(rotation=90) 
    #hue:將組別以顏色分開
    #size:將組別以大小分開
    #style:將組別以樣式分開
    #https://seaborn.pydata.org/generated/seaborn.scatterplot.html
#子紙圖調整
ax1.set_xticks([0,5,10,15,20,25,30]) 
    # 設置 x 軸刻度呈現 label 的位置
    #rotation= '90'等同 rotation='vertical'
ax1.set_ylim([-5,10]) # 設置 y 軸的範圍
ax1.set_xticklabels(['one','two','three','four','five','six','seven'],
rotation=30, fontsize='small')
ax2.legend(loc = 'best')#不知道是什麼
# 設置 x 軸刻度的 label
ax1.set_title('my first plot') # 設置 subplot 的 title
ax3.set_xlabel('123') # 設置 subplot x 軸 的 label
#畫圖範例(1)
data = pd.read_csv('C:/Users/Lin ting yu/Desktop/Python(2)/spx.csv',index_col=0, parse_dates=True)
spx = data.iloc[:,0] # or using data['spx']
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(spx)
fig
crisis_index=[(datetime(2007,10,11),'peak of bull market'),
              (datetime(2008,3,12),'Bear Stearns Fails'),
              (datetime(2008,9,15),'Lehman Bankruptcy')]
#畫圖範例(1)---標點
for date, label in crisis_index:
    ax.annotate(label
                ,xy=(date,spx.asof(date)+50)#標記點+文字的位子
                ,xytext=(date,spx.asof(date)+20)
                ,arrowprops=dict(facecolor='yellow')#箭頭
                ,horizontalalignment='left',verticalalignment='top')#讓箭頭反過來
    #https://www.itread01.com/content/1544608110.html
    #這裡有所有解說
#畫圖範例(1)---圖片儲存
plt.savefig('C:/Users/Lin ting yu/Desktop/Python(2)/spx.png',
dpi=400, bbox_inches='tight')
#畫圖範例(2)
z = DataFrame(np.random.randn(800).reshape([400,2]),columns=['series 1','series 2'])
   #比較 y= DataFrame(np.random.randint(0,2,(400,2)),columns=['series 1','series 2'])
plt.figure(1)
z.plot.scatter(x='series 1', y='series 2')
plt.scatter(z.iloc[:,0],z.iloc[:,1]) 
#畫圖範例(2)---(方法二)
fig,axes = plt.subplots(2,1)
z.plot.scatter(x='series 1', y='series 2',ax=axes[0]) 
    #用fig可以叫得出來
#網路抓資料---資料庫(可以用來下載 google finance,St.Louis FED (FRED), World Bank, OECD, Eurostat)
    #如何知道資料庫名子??
'''
此為XML viewer：可以將HTML檔自動排版
https://codebeautify.org/xmlviewer
此為http狀態碼之查表碼
https://codebeautify.org/xmlviewer

在chrome(一定要是chrome)中，輸入
http://httpbin.org/user-agent
即可得到你的電腦head
'''
#基礎爬蟲
myHead={'usere-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
print(rq_1.headers['content-type'])#查詢網站之格式
print(rq_1.encoding)#查詢編碼器
#print(bs_1.title.getText)
#基礎爬蟲--範例:自由時報
urL_1 ="https://paper.udn.com/papers.php?pname=PID0001"
rq_1=requests.get(urL_1)
#urL後面加,auth=('user', 'pass')，輸入的帳號密碼
rq_1.encoding='utf-8'
bs_1= BeautifulSoup(rq_1.text,'lxml')#不知道為甚麼html5lib不能使用
#將抓取的資料存成字典型態(範例:自由時報)
for i in bs_1.find_all('div','history_list'):
    for j in i.find_all('li','subject'):
        key=j.text.strip()
        value_1=j.a['href']
    for j in i.find_all('li','date'):
        value_2=j.text
        dict[key]=[value_1,value_2]
#將資料存成json檔(範例:自由時報)
with open('ltnnews.json',"w",encoding='utf-8') as filE:
    json.dump(newS,filE,ensure_ascii=False,indent=4)

with open('ltnnews.json',"r",encoding='utf-8') as filE:
    ltnNews=json.load(filE)  

#將資料存成csv檔(範例:自由時報)
for i in bs_1.find_all('div','history_list'):
    try:
        
        for j in i.find_all('li','subject'):
            titlE=j.text.strip()
            linK=j.a['href']
            #writeR.writerow((titlE,linK))
        for j in i.find_all('li','date'):
            timE=j.text
            writeR.writerow((timE,titlE,linK))
    except:
        continue
csv_filE.close()

#基礎爬蟲--範例:ptt
urL_2="https://www.ptt.cc/bbs/Gossiping/index.html"
myCookies= {"over18":"1"}#詳見cookies筆記之圖片
rq1 = requests.get(urL_1,headers=my_heaD)
rq2 = requests.get(urL,headers=my_heaD,cookies=myCookies)#有cookies
#
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
data1 = web.DataReader('GDP','fred', start, end)
    #'fred'是什麼??
inflation = web.DataReader(['CPIAUCSL', 'CPILFESL'], 'fred', start, end)
mathces = wb.search('co2')
dat = wb.download(indicator='EN.ATM.CO2E.EG.ZS', start=2005, end=2008)
#網路抓資料----google 搜尋趨勢
pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload(kw_list=['柯文哲','韓國瑜'], timeframe='all',
geo='TW',gprop='')
    #timeframe=時間區段
    #geo=地理區域，https://www.gegeurope.com/Pages/CountryCode.htm
    #gprop:images，news，youtube或froogle（對於谷歌購物搜索結果）
data_gtrend=pytrends.interest_over_time()
    #將抓到的資料轉成DataFrame
    #isPartial 是什麼??
data_gtrend.plot()
plt.show()
pytrends.related_topics()
    #pytrends.related_topics() 不知道是什麼???
#網路抓資料----從API抓資料
df_tiingo= pdr.get_data_tiingo('GOOG',start = 'JAN-01-2020' ,
api_key=('4fbbfe771a76e7b1a00a56ea5a5ab24268d4e47c'))
    #freq 不知道怎麼使用
    #時間: ‘JAN-01-2010’, ‘1/1/10’, ‘Jan, 1, 1980’. Default is ‘1/1/2010’.
#迴圈---if
x= int(input('請輸入x'))#而輸入的東西不管是文字或是數字接儲存為字串
y = int(input('請輸入y'))
z = int(input('請輸入z'))
if x < y and x < z:
    print('x 是最小的')
elif y < z:
    print('y 是最小的')
else:#要加":"
    print('z 是最小的')
#迴圈---while
N=int(input('請輸入一個正整數'))
x = 1
iter = 2
while (iter <= N):#iter 大於等於 N時為true
    x = x + iter
    iter = iter + 1
print(x)
#迴圈---for
N=int(input('請輸入一個正整數'))
x = 1
for ii in range(2,N+1,1): 
    x=x+ii
a=['a','b','c']
for ii,a in enumerate(a):
    print(ii, a)
#迴圈----try
for i in range(1000):
    success = np.random.randint(11) # discrete uniform distributed
    failure= 10- success
    try: # try block
        ratio = round(success/failure,10)
        print('the success/ failure ratio is',ratio)             
    except ZeroDivisionError: # exception block
        print('the ratio is undefined')
#迴圈---範例
while True:#while 可以使此程式碼直行完後還存在
    val = input('Enter an integer: ')
    try:
        val = int(val)
        print('The square of the number entered is', val**2)
        #break # exit the while loop(沒有可以重複好幾次，如同去掉while) 
    except ValueError:
        print(val, 'is not an integer')
    #if   :要執行,分類於 A或B(條件自訂)
    #try  :要執行,分類於 A或B(條件原於結果)
    #while:是否要執行(條件為true或fale)
    #for  :要執行,重複執行(規律的模式)
#function
pi = 3.14159
def Volume(radius,hight = 1): # 圓體積
    if isinstance(hight, int):
        hight = hight
    return pi*(radius**2)*hight
#用文字檔進行存取
#Simulation---一致性
N0 = [50,100,500,2000]
R = 2000
xbar = np.zeros([R,1])
fig1, axs = plt.subplots(2,2,sharex=True, sharey=True)
fig1.suptitle('Simulation results of '+r'$\bar{X}$',fontsize=10)
for jj, N in enumerate(N0):# enumerate:同時表示N0的內容的順序和內容
    for ii in range(R):
        x = 2+np.random.randn(N)
        xbar[ii,0] = np.mean(x)
    if jj<2:
        axs[0,jj].hist(xbar)
        axs[0,jj].axvline(x=np.mean(xbar),color='red')
        axs[0,jj].set_title('N='+str(N),fontsize=10)
        axs[0,jj].tick_params(axis='both', which ='major',labelsize=10)
    if jj>=2:
        axs[1,jj-2].hist(xbar)
        axs[1,jj-2].axvline(x=np.mean(xbar),color='red')
        axs[1,jj-2].set_title('N='+str(N),fontsize=10)
        axs[1,jj-2].tick_params(axis='both',which ='major', labelsize=10)
fig1.set_size_inches(7.5, 5)
    #plt.savefig(path+'/fig.png', dpi=100, bbox_inches='tight')
    #畫圖:https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.tick_params.html
#Simulation---pdf
N0 = [2000]
R = 2000
x_axis = np.arange(-4, 4, 0.001)
xbar = np.zeros([R,1])
for ii in range(R):
    x = 2+np.random.randn(N)
    xbar[ii,0] = np.mean(x)
fig2, axs = plt.subplots(1)
fig2.suptitle('Simulation results of '+r'$\bar{X}$'+', N='+str(N),fontsize=7)
axs.plot(x_axis, norm.pdf(x_axis,0,1))
axs.hist(np.sqrt(N)*(xbar-2), bins=100,density=True)
axs.axvline(x=1.645,color='red')
axs.axvline(x=-1.645,color='red')
axs.tick_params(axis='both', which='major', labelsize=10)
fig2.set_size_inches(5, 2.5)
#迴歸-
path = r'C:/Users/Lin ting yu/Desktop/Python(2)'
team = pd.read_csv(path+'\\Teams.csv',header = 0)
mlb_all = pd.read_csv(path+'\\Teams.csv',header = 0)
mlb_all['win_odd'] = mlb_all['W']/mlb_all['G']
mlb_all['bav'] = mlb_all['H']/mlb_all['AB']
#迴歸---ols方法一(import statsmodels.formula.api as smf)
ols_results = smf.ols('win_odd~ERA+bav', data = mlb_all ).fit()
print(ols_results.summary())
#迴歸---ols方法二(import statsmodels.api as sm)
X = np.column_stack((mlb_all['ERA'],mlb_all['bav']))
X = sm.add_constant(X)
results = sm.OLS(mlb_all['win_odd'],X ).fit()
print(results.summary())
#迴歸---t-test
era = mlb_all['ERA'].groupby(mlb_all['lgID'])
    #mlb2018['ERA']以mlb2018['lgID']的方式分組
    #https://cloud.tencent.com/developer/article/1193823
era_AL = mlb_all.loc[mlb_all.lgID=='AL',['ERA']]
    #將列 = 'AL'的取出，且只選 ['ERA']這列
era_NL = mlb_all.loc[mlb_all.lgID=='NL',['ERA']]
result = statsmodels.stats.weightstats.ttest_ind(era_AL, era_NL,alternative='two-sided')
    #只要是"pandas.core.frame.DataFrame"就可以跑
    #https://www.itread01.com/content/1546486926.html 
    # tstat (float) and pvalue of the t-test
#迴歸---(習題)團隊勝率(W/G)和投手防禦率(ERA)或是打擊(H/AB)是否有正向(反向)關係?
#迴歸---(習題)國聯(LA)團隊打擊率是否比美聯(AL)不好?
#迴歸---如果想讓勝場數變多，應該注重打擊還是注重投手?
#迴歸---追蹤資料分析 
    #(假定 yit 和 xit 的關係不會隨時間 (年度) 變動，因此係數 beta並沒有下標 t)
result = smf.ols('win_odd~ERA+bav',data = mlb_all[(mlb_all['yearID']<=2018)& (mlb_all['yearID']>=1950)]).fit()
    # 限定分析年度範圍為 1950 至 2018 年
#迴歸---橫斷面分析 
    #(假定 yit 和 xit 的關係會隨時間 (年度) 變動，因此係數 beta有下標 t)
results = [None]*(2018-1950)
beta_era = np.zeros(((2018-1950),1))
beta_bav = np.zeros(((2018-1950),1))
beta_era_ci = np.zeros((2018-1950,2))
beta_bav_ci = np.zeros((2018-1950,2))
jj=0
for ii in range(1950,2018,1):
    results[jj] = smf.ols('win_odd~ERA+bav',data = mlb_all[mlb_all['yearID']==ii]).fit()
    beta_era[jj,0] = results[jj].params[1]#存入beta1
        #.params[1] :[0]是截距，依此類推
    beta_bav[jj,0] = results[jj].params[2]#存入beta2
    beta_era_ci[jj,0:2] = np.array(results[jj].conf_int().iloc[1,], ndmin = 2)
        #conf_int():信心水準(默認95%),1為左邊
        #ndmin:幾維陣列 e.g:[[1 2 3]]為2維陣列 
    beta_bav_ci[jj,0:2] = np.array(results[jj].conf_int().iloc[2,], ndmin = 2)
        #2為右邊(95%信心水準)
    jj=jj+1
df_era = pd.concat([pd.DataFrame(beta_era),pd.DataFrame(beta_era_ci)],axis=1)
df_bav = pd.concat([pd.DataFrame(beta_bav),pd.DataFrame(beta_bav_ci)],axis=1)

df_era.index = pd.date_range(start='1950',end='2018',freq='A')
df_bav.index = pd.date_range(start='1950',end='2018',freq='A')
#迴歸---畫出信心水準
plt.plot_date(df_era.index, df_era.iloc[:,0], '-')
d = df_era.index
plt.fill_between(d, df_era.iloc[:,1], df_era.iloc[:,2],facecolor='green',
alpha=0.2, interpolate=True)
    #將interpolate設置為True將計算實際的相交點，並將填充區域擴展到該點。
plt.show()

plt.plot_date(df_era.index, df_bav.iloc[:,0], '-')
d = df_bav.index
plt.fill_between(d, df_bav.iloc[:,1], df_bav.iloc[:,2],facecolor='green',
alpha=0.2, interpolate=True)
plt.show()

#迴歸---二元迴歸模型(smf.Logit)
# 將 y 變數 (世界大賽勝利與否) 進行編碼為類別變數

y=pd.Categorical(mlb_all.loc[(mlb_all.yearID>=1950) & (mlb_all.yearID!=1994),'WSWin'])
#(由於 1994 年並沒有進行世界大賽因此排除)
y=y.codes
X=mlb_all.loc[(mlb_all.yearID>=1950) & (mlb_all.yearID!=1994),['ERA','bav']]
model = smf.Logit(y, X) # Logit model
result = model.fit()
print(result.summary())
result.get_margeff(at='overall').margeff # marginal effects
#file
mlbdata={'mlb2018':mlb2018}
import pickle # used to save the data
    # pickle a variable to a file
file = open('C:\\Users\\Lin ting yu\\Desktop\\Python(2)\\mlb2018.pickle', 'wb')
    #在指定的地方開一個mlb2018.pickle的檔案
pickle.dump(mlbdata, file)#將資料存入此
file.close()
    # open the data
with open('C:\\Users\\Lin ting yu\\Desktop\\Python(2)\\mlb2018.pickle','rb') as file:data =pickle.load(file)
    #不知道file在幹嘛(優勢)
#資料轉換---標準化
def nor(x): 
    y = (x-np.mean(x))/np.std(x)
    return y
mlb_all['n_bav'] = nor(mlb_all['H']/mlb_all['AB'])
#資料轉換---取自然對數
mlb_all['lg_bav'] = log(mlb_all['H']/mlb_all['AB'])
#資料轉換---二元迴歸模型(smf.Logit)  y 變數 (世界大賽勝利與否)
y=pd.Categorical(mlb_all.loc[(mlb_all.yearID>=1950) & (mlb_all.yearID!=1994),'WSWin'])
    #(由於 1994 年並沒有進行世界大賽因此排除)
y=y.codes
X=mlb_all.loc[(mlb_all.yearID>=1950) & (mlb_all.yearID!=1994),['ERA','bav']]
model = sm.Logit(y, X) # Logit model
result = model.fit()
print(result.summary())
result.get_margeff(at='overall').margeff # marginal effects
    #https://www.statsmodels.org/dev/generated/statsmodels.discrete.discrete_model.DiscreteResults.get_margeff.html
#PSFD 華人家庭動態資料庫 (Panel Study of Family Dynamics)
path = r'C:/Users/Lin ting yu/Desktop/Python(2)'    
data = pyreadstat.read_dta(path+'/RI1999_v201703_stata.dta')

Df = DataFrame(data[0][['x01', 'x06', 'a01', 'a02', 'a04a', 'b01', 'c01', 'c04a01', 'c04a02', 'c08', 'd01z01'
, 'd01z02', 'd13', 'j01','j02z02c1', 'j02z02c2','j02z02c3','j02z02c4']]) 
Df = Df.replace( [6,96,996,9996,7,97,997,9997,8,98,998,9998,9,99,999,9999,0,00,000,0000], np.nan)
    #把這些變na
plt.hist(Df.loc[Df.d01z01==3,'a02'],density=True)
plt.hist(Df.loc[Df.c01==1,'a02'],density=True,alpha=0.4,label='have a job')
plt.hist(Df.loc[Df.c01==2,'a02'],density=True,alpha=0.4,label='do NOT have a job')
    #density=True :直方圖的總和將歸一化為1
    #density=True :
    #(問題)為什麼3個圖可以疊在一起
plt.legend(loc='upper left')
    #把label顯示在上面    
#PSFD ---探討不同職業與小孩個數的關係
fig1, axe = plt.subplots(1,1)
plt.scatter(x='b01', y='j01', data=Df.loc[(Df.a02<47) & (Df.a02>=40)])
plt.title('With duplicate records', weight='bold', fontsize=16)
    #fig1.set_size_inches()
    #改變大小
    #save_path = ('.../Week11')
    #plt.savefig(save_path+'/fig1.png',dpi=400,bbox_inches='tight')
    #存圖
fig2, axe = plt.subplots(1,1)
sns.catplot(x='b01', y='j01', data=Df.loc[(Df.a02<47) & (Df.a02>=40)],aspect=2)
plt.title('With duplicate records', weight='bold', fontsize=16)
fig2.set_size_inches(1,0.5)
    #plt.savefig(save_path+'/fig2.png', dpi=400, bbox_inches='tight')
#從證交所網站抓資料
import requests
    #https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
    # 從證交所網站上獲取指定日期的所有個股資訊
url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date='
resp = requests.get(url+'type=')
data = resp.json()
    # json是一種格式檔
types = ['text', 'float', 'int', 'int']
    #['成交統計','成交金額(元)','成交股數(股)','成交筆數',]
#網頁抓取後編碼錯誤?
resp.encoding = 'utf-8'    #轉換編碼至UTF-8
resp.encoding = 'big5' #設定成該網頁的編碼，例如big5編碼或簡體的gbk編碼
#yahoo上抓台積電的資料
import requests
import json
import numpy as np
import pandas as pd
site = "https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"
    #2330.TW 是台積電在 yahoo finance 上的 symbol，你也可以任意換成其他的，例如蘋果（AAPL），特斯拉（TSLA），微軟（MSFT）等等
    #period1 是指起始時間，其單位為從1970年開始過了n秒
    #period2 是指結束時間，其單位為從1970年開始過了n秒
response = requests.get(site)
print(response.text)
data2 = json.loads(response.text)
    # json是一種格式檔
df = pd.DataFrame(data2['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(np.array(data2['chart']['result'][0]['timestamp'])*1000*1000*1000))
df.head()
    #https://www.finlab.tw/%E7%94%A8%E7%88%AC%E8%9F%B2%E7%88%AC%E5%85%A8%E4%B8%96%E7%95%8C%E8%82%A1%E5%83%B9/


#從yahoo電影上抓評分與評語(目前還不知道怎麼抓)
    #https://movies.yahoo.com.tw/movieinfo_review.html/id=9597
import requests
from bs4 import BeautifulSoup
allcomments=[] # 建立一個空 list 存放所有的評論
allscores=[] # 建立一個空 score 存放所有的評分
path = 'https://movies.yahoo.com.tw/movieinfo_review.html'
id_ = 'id=9597'
for ii in range(1,19): # 頁數跳換
    page = str(ii)
    resp = requests.get(path+id_+'?sort=update_ts&order=desc&page='+page)
    #?sort=update_ts&order=desc&page=
    #上面那串進入網頁原始碼才會出現
    soup = BeautifulSoup(resp.text,'html.parser')
    #解析html的3種方法
    #html.parser:舊方法，相容性差
    #lxml:速度快，相容佳
    #html5lib:速度慢解析強，需另裝html5lib
    soup_span = soup.find_all('span',class_='') 
    # 儲存有 span 的地方，且不存在任何 class 屬性 (評論部分)
    x=soup.find_all('input', {'name': 'score'}) 
    # 儲存有 input 的地方，且 name 屬性為 score(評分部分)
    #http://blog.castman.net/%E6%95%99%E5%AD%B8/2016/12/22/python-data-science-tutorial-3.html
    lines = [span.get_text().strip().replace('\r\n', ' ') for span in soup_span]
    # 一行一行擷取文字
    i1 = lines.index('網友短評') # 找出網友短評位置 (900行)
    try:
        i2 = lines.index('上一頁') # 找出上一頁位置
    except ValueError:
        if lines.index('...')>lines.index(page):
            i2 = lines.index(page)
        else:
            i2 = lines.index('...')
    comments = lines[i1+1:i2] # 真正存放評論的地方
    allcomments = allcomments+comments
    score=[]
    for value in x: # 把 inuput 中的 value 都抓出來 (分數)
        score+= value.get('value')
    score = score[1:]
    for jj in range(len(score)):
        if int(score[jj])>=4: # 若大於 4 則儲存為正評
            score[jj]=score[jj].replace(score[jj], '正評')
        else:
            score[jj]=score[jj].replace(score[jj], '負評')
    allscores = allscores+score



import requests
from bs4 import BeautifulSoup
path = 'https://movies.yahoo.com.tw/movieinfo_review.html'
id_ = 'id=9597'
resp = requests.get(path+id_+'?sort=update_ts&order=desc&page=')
    #?sort=update_ts&order=desc&page=
    #上面那串進入網頁原始碼才會出現
soup = BeautifulSoup(resp.text,'html.parser')
    #解析html的3種方法
    #html.parser:舊方法，相容性差
    #lxml:速度快，相容佳
    #html5lib:速度慢解析強，需另裝html5lib
soup_span = soup.find_all('a') 
print()
    
#41~63   @基本元素(tuber,list,range,矩陣)
#64~73   @矩陣(抓資料,)
#74~83   @series,字典
#84~121  @DataFrame(合併,加行列,刪資料,整理(groupby),運算,敘述統計與排序)
#122~139 @Time Series(時間,合併)
#140~170 @Panel Data(匯入資料,excell,missing values)
#171~227 @畫圖(創圖紙,圖紙調整,子紙,子紙圖調整)  
#228~259 @畫圖範例(圖片儲存,標點,圖片儲存)
#260~287 @網路抓資料(google 搜尋趨勢,從API抓資料)
#288~333 @迴圈(if,for,while,try)
#334~340 @function
#340     @用文字檔進行存取
#341~379 @Simulation(一致性,pdf)
#380~448 @迴歸(ols法一,ols法二,t_test,(習題)*3,追蹤資料分析 ,橫斷面分析,畫出信心水準)
#450~461 @file
#


#連結
#14 @其他API資料: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html
#tiingo:'4fbbfe771a76e7b1a00a56ea5a5ab24268d4e47c'


#問題
#45,50,224,261,265,278,282,471,502


#(問題)團隊勝率(W/G)和投手防禦率(ERA)或是打擊(H/AB)是否有正向(反向)關係?
mlb2018['win_odd'] = mlb2018['W']/mlb2018['G'] # 計算勝率 (勝場/出賽場數)
fig1, axes = plt.subplots(1,2)
sns.scatterplot(x='bav', y='win_odd', data=mlb2018, ax=axes[0])
    #era:防禦率 bav:打中數(H)/打擊數(AB)   
sns.scatterplot(x='ERA', y='win_odd', data=mlb2018, ax=axes[1])
plt.subplots_adjust(left=0.1,right=0.9,bottom=0.1,wspace=0.4,hspace=0.1)

#正規表示式之練習網站
#https://www.regexpal.com/

#問題
'''
google圖片|蝦皮網的資訊|  為什麼抓不下來?





'''
