#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
def get_page(url,f,header=header):
    resp = requests.get(url,headers=header).text
    soup = BeautifulSoup(resp,"lxml")
    trs = soup.find('table',class_="table table-bordered table-striped").find_all('tr')
    for tr in trs:
        ips = tr.find_all('td')
        if ips == []:
            continue
        else:
            ip_adress = ips[0].string
            ip_port = ips[1].string
            ip_anony = ips[2].string
            ip_type = str(ips[3].string)
            ip_type = ip_type.lower()
            ip_location = ips[4].string
            ip_speed = ips[5].string
            ip_last_time = ips[6].string
            f.write("{},{},{},{},{},{},{}\n".format(ip_adress,ip_port,ip_anony,ip_type,ip_location,ip_speed,ip_last_time))
def main(page_num):
    local_time = time.localtime(time.time())
    with open("快代理最新ip地址.csv","w",encoding="utf_8_sig") as f:
        f.write("爬取时间：{}\n".format(time.strftime("%Y %b %d %a %H:%M:%S ", time.localtime())))
        f.write("{},{},{},{},{},{},{}\n".format('地址', 'PORT', '匿名度', '类型', '位置', '响应速度', '最后验证时间'))
        for i in range(1,page_num):
            url = 'https://www.kuaidaili.com/free/inha/{}/'.format(str(i))
            get_page(url,f)
            time.sleep(2)
            print("爬取进度：{}/{}".format(str(i),str(page_num-1)))
if __name__ == '__main__':
    main(101)