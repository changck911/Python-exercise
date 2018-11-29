# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:50:53 2018

@author: HChang

@title: RW file
"""

import os;

path = os.path.abspath('.\\data');

if not os.path.isdir(path):
    os.mkdir(path);
#寫入
#r - 讀取(檔案需存在)
#w - 新建檔案寫入(檔案可不存在，若存在則清空)
#a - 資料附加到舊檔案後面(游標指在EOF)
#r+ - 讀取舊資料並寫入(檔案需存在且游標指在開頭)
#w+ - 清空檔案內容，新寫入的東西可在讀出(檔案可不存在，會自行新增)
#a+ - 資料附加到舊檔案後面(游標指在EOF)，可讀取資料
#b - 二進位模式
f = open(path+'\\test.txt','w');
f.write('test123');
f.close();
#讀取
f = open(path+'\\test.txt','r');
print(f.read());
f.close();