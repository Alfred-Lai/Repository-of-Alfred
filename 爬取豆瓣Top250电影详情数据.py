#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import requests
from bs4 import BeautifulSoup
start_time = time.time()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
#获取单页所有电影详情页面的链接
def get_detail_url(url,header):
    resp = requests.get(url,headers=header).text
    html = BeautifulSoup(resp,"lxml")
    lis = html.find('ol',class_='grid_view').find_all('li')
    for li in lis:
        film_name = li.find('span',class_='title').string
        detail_url = li.find('a')['href']
        info[film_name] = detail_url
    return lis
#获取所有Top250电影详情页面的链接
def get_all_url():
    global info
    info = {}
    count = 0
    while True:
            url = 'https://movie.douban.com/top250?' + 'start={}&filter='.format(str(count))
            lis = get_detail_url(url,header)
            if lis == []:
                break
            else:
                count += 25
    return info
#解析详情页面数据
def get_detail(url,header,f):
    resp = requests.get(url,headers=header).text
    soup = BeautifulSoup(resp,"lxml")
    #名称
    name = soup.find('div', id="content").find('h1').find('span').stripped_strings
    name = "".join(name)
    try:
        name = name.replace(",","")
    except:
        name = name
    #导演
    director = list(soup.find('div',id='info').find('span',class_="attrs").stripped_strings)
    director ="".join(director)
    #编剧
    try:
        scriptwriters = set(list(soup.find('div',id='info').find_all('span',class_="attrs")[1].stripped_strings))
        scriptwriters = list(scriptwriters)
        try:
            scriptwriters.remove('/')
            scriptwriters = "/".join(scriptwriters)
        except:
            scriptwriters = "/".join(scriptwriters)
    except:
        scriptwriters = '无编剧'
    #演员
    try:
        actors = set(list(soup.find('div',id='info').find_all('span',class_="attrs")[2].stripped_strings))
        actors = list(actors)
        try:
            actors.remove('/')
            actors = "/".join(actors)
        except:
            actors = "/".join(actors)
    except:
        actors = "演员信息缺失"
    #评分
    score = list(soup.find('strong',class_="ll rating_num").stripped_strings)
    score = "".join(score)
    #上映时间
    dates = soup.find('div',class_="subject clearfix").find_all('span',property='v:initialReleaseDate')
    data = []
    for date in dates:
        data.append(list(date.stripped_strings)[0])
    data = "/".join(data)
    #简介
    summary = list(soup.find('div',class_="related-info").find('span',property="v:summary").stripped_strings)
    summary = "".join(summary)
    f.write('《{}》,{},{},{},{},{},{}\n'.format(name,director,scriptwriters,actors,score,data,summary))

def main():
    info = get_all_url()
    count = 0
    with open("Top250_data.csv","w",encoding="utf_8_sig") as f:
        f.write('{},{},{},{},{},{},{}\n'.format('name','director', 'scriptwriters', 'actors', 'score', 'data', 'summary'))
        for key in info:
            url = info[key]
            get_detail(url,header,f)
            count += 1
            print("爬取进度：{}/250".format(str(count)))
if __name__ == '__main__':
    main()
finish_time = time.time()
print("程序运行时间为：{}".format(str(finish_time - start_time)))
