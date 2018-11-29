# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:07:00 2018

@author: HChang

@title: wikipedia url catch
"""

import urllib.request
from bs4 import BeautifulSoup as bs
import re

"""定義要抓取的網址"""
URL = "https://en.wikipedia.org/wiki/The_Matrix"
"""抓取網頁"""
response = urllib.request.urlopen(URL)
"""查看網頁資訊"""
#print(response)
"""查看網頁內容"""
#print(response.read())
"""將網頁內容做成湯"""
html_cont = response.read()
soup = bs(html_cont,'lxml',from_encoding='utf-8')
"""顯示網頁標頭"""
#print(soup.title)
"""顯示湯的內容"""
#print(soup.prettify())
"""隱藏標籤並顯示標籤內內容"""
#print(soup.get_text())
"""尋找某個標籤之第一個以<a>為例"""
#print(soup.find('a'))
"""尋找某個標籤以<a>為例(陣列)"""
#contents = soup.find_all('a')
#for content in contents:
#    print(content)
"""尋找某個標籤並輔以regular expression以<a>為例"""
contents = soup.find_all('a',href=re.compile("^/wiki/\w+"))
for content in contents[:10]:
    """排除不必要的東西"""
    if not re.search("\w+:\w+",content['href']):
        print(content['href'])
#print("========= result: =========");
