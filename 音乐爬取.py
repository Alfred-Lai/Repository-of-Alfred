#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 2/7/2020 6:57 PM
@Author  : Alfred Lam
@FileName: 音乐爬取.py
@Software: PyCharm
"""
import os
import queue
import re
import requests
import threading
import time
from urllib import request
from bs4 import BeautifulSoup

start_time = time.time()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.87 Safari/537.36',
    'Cookie': 'UM_distinctid=1701f4fb65f4bd-08fc81a90b488-b791b36-e1000-1701f4fb660524; '
              'CNZZDATA4381083=cnzz_eid%3D1404935375-1581070979-null%26ntime%3D1581070979; '
              'bdshare_firstime=1581073293202; Hm_lvt_2eb9199e975e2f2a842a69f2ebf1e274=1581073283,1581073293,'
              '1581073354; Hm_lpvt_2eb9199e975e2f2a842a69f2ebf1e274=1581073354 '
}


class Producer1(threading.Thread):  # 生产者1，用于从主页面获取所有音乐单独页面的链接
    def __init__(self, page_url, url_container, *args, **kwargs):
        super(Producer1, self).__init__(*args, **kwargs)
        self.page_url = page_url
        self.url_container = url_container

    def run(self) -> None:
        resp = requests.get(self.page_url, headers=header).text
        soup = BeautifulSoup(resp)
        ul = str(soup.find_all('ul', class_="li clearfix"))
        contents = re.findall('''
        .+?<li.+?box_l".+?ef="(.+?)"    # 音乐页面链接
        .+?title="(.+?)"    # 音乐名称
        ''', ul, re.DOTALL | re.VERBOSE)
        for content in contents:
            name = content[1]
            link = 'http://www.4399er.com' + content[0]
            self.url_container.put({"name": name, "link": link})


class Producer2(threading.Thread):  # 生产者2，用于从每个单独的音乐页面链接获取音乐源的地址和歌词
    def __init__(self, url_container, musicurl_container, *args, **kwargs):
        super(Producer2, self).__init__(*args, **kwargs)
        self.url_container = url_container
        self.musicurl_container = musicurl_container

    def run(self) -> None:
        while True:
            try:
                music_page_url = self.url_container.get(timeout=10)
                music_name = music_page_url["name"]
                music_page_url = music_page_url["link"]
                resp = requests.get(music_page_url, header).text
                soup = BeautifulSoup(resp)
                content = str(soup.find('div', class_="music__play-audio"))
                try:
                    true_url = re.search('''
                    <div.+?value.+?current.+?ong=(.+?)&
                    ''', content, re.VERBOSE | re.DOTALL).group(1)  # 部分网页源码不符合规律，无法读取到
                    true_url = re.sub("http:", "", true_url)
                    true_url = 'http:' + true_url
                    self.musicurl_container.put({"music_name": music_name, "dow_url": true_url})
                except Exception as e:
                    print(e.args)
                    print("%s音乐由于网页源代码不符合规律(提取标识符1)，地址提取失败！" % music_name)
            except Exception as e:
                print(e)
                break


class Consumer(threading.Thread):
    def __init__(self, container, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.container = container

    def run(self) -> None:
        while True:
            try:
                dow_urls = self.container.get(timeout=10)
                name = dow_urls["music_name"] + '.mp3'
                dow_url = dow_urls["dow_url"]
                try:
                    request.urlretrieve(dow_url, os.path.join("music", name))
                    print("%s已成功下载了音乐：%s" % (threading.current_thread().name, name))
                except Exception as e:
                    print(e.args)
                    print("(提取标识符2)因为urltrieve的原因，%s没有成功下载音乐：%s" % (threading.current_thread().name, name))
            except Exception as e:
                finish_time = time.time()
                print("%s已结束，运行时间为%d" % (threading.current_thread().name, finish_time-start_time))
                print(e)
                break


def main():
    start_url = 'http://www.4399er.com/xzt/xmblcq/'
    url_container = queue.Queue()   # 用于在Producer1中存储所有音乐页面链接，给Producer2用
    music_original_container = queue.Queue()    # 用于在Producer2中存储音乐源的链接，给Consumer下载用

    th1 = Producer1(start_url, url_container)
    th1.start()

    for x in range(3):
        th2 = Producer2(url_container, music_original_container)
        th2.start()

    for x in range(5):
        th3 = Consumer(music_original_container, name="下载线程%d号" % x)
        th3.start()


if __name__ == '__main__':
    main()
