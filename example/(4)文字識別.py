from nltk.book import *#將範例的書本載入

#text3.concordance("lived")
#text1.similar("monstrous")
#print(len(set(text4))/ len(text4))#計算文字重複率


import nltk
import jieba
def lexical_diversity(text):
 return len(set(text)) / len(text)
#raw=open("⽂字.txt",encoding="utf-8").read()
raw="""陪你熬夜　聊天到爆肝也沒關係 陪你逛街　逛成扁平⾜也沒關係 超感謝你　
讓我重⽣　整個ORZ 讓我重新認識　love love love 戀愛ing happy ing
⼼情就像是　坐上⼀台噴射機 戀愛ing　改變　ing　改變了黃昏　黎明　
有你　都⼼跳到不⾏ 你是空氣　但是好聞勝過了空氣 你是陽光　
但是卻能照進半夜裡 ⽔能載⾈　也能煮粥　餵飽了⽣命 你就是維他命　
love love love 戀愛ing happy ing　⼼情就像是　坐上⼀台噴射機 戀愛ing
改變　ing　改變了黃昏　黎明　有你　都⼼跳到不⾏ 未來某年某⽉　
某⽇某時　某分某秒　某⼈某地　某種永遠的⼼情 不會忘記此刻　
love love love love love love love 戀愛ing happy ing　⼼情就像是　
坐上⼀台噴射機 戀愛ing　改變　ing　改變了黃昏　黎明　有你　
都⼼跳到不⾏ 黃昏　黎明　整個都戀愛ing"""
single=nltk.text.Text(jieba.cut(raw))
print(lexical_diversity(single))