#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import  BeautifulSoup
from selenium import webdriver
import time
time_start = time.time()
url = 'http://news.tsinghua.edu.cn/publish/thunews/10303/index.html'
browser = webdriver.Chrome(executable_path='C:\\Users\\Honor\\Desktop\\Project in PC\\chromedriver\\chromedriver')
#strhtml = requests.get(url)
browser.get(url)
strhtml = browser.page_source
browser.close()
#strhtml.encoding = 'gbk'
soup = BeautifulSoup(strhtml,'lxml')
data = soup.select('body > div > div > section.colunm1 > ul > li > figure > figcaption > a')
f = open('清华新闻爬取.txt','w',encoding= 'utf-8')
for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href')
    }
    f.write(str(result)+'\n')
    print(str(result))
f.close()

for i in range(2,585):
    url = 'http://news.tsinghua.edu.cn/publish/thunews/10303/index_' + str(i) + '.html'
    browser = webdriver.Chrome(executable_path='C:\\Users\\Honor\\Desktop\\Project in PC\\chromedriver\\chromedriver')
    browser.get(url)
    strhtml = browser.page_source
    browser.close()
    soup = BeautifulSoup(strhtml, 'lxml')
    print(soup)
    data = soup.select('body > div > div > section.colunm1 > ul > li > figure > figcaption > a')
    print(data)
    f = open('清华新闻爬取.txt', 'a',encoding = 'utf-8')
    for item in data:
        result = {
            'title': item.get_text(),
            'link': item.get('href')
        }
        f.write(str(result) + '\n')
        print(str(result))
    f.close()
    print("爬取进度为：{}/584".format(i))
time_end = time.time()
print("爬取所用总时间为：{}".format(time_end - time_start))