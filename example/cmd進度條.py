import os
import time

def progressBarDisplay(miniNum, maxNum, addNum):
    '''
     作者:小蓝枣
     作用:模拟进度条
     参数1:最小值
     参数2:最大值
     参数3:递增比例
    '''
    # 填充符号
    fill_symbol = "#"
    # 默认符号
    default_symbol = "-"
    # 进度条长度
    bar_length = int((maxNum-miniNum)/addNum)
    for i in range(0, bar_length + 1, 2):
        # 【核心】清除屏幕
        os.system('cls')
        print("下載進度條: [" + i * fill_symbol + (bar_length - i) * default_symbol + "]")
        print("進度百分比: (" + str(int((i / bar_length)*100)) + "%)")
        # 延迟
        time.sleep(0.5)

progressBarDisplay(0, 100, 2)
