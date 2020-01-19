#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
from jsonpath import jsonpath
def bilibili_fav(page):
    url = 'https://api.bilibili.com/x/space/bangumi/follow/list?'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Cookie': "_uuid=72D7850B-BA80-2A8D-3C2C-DA8312751A9A65760infoc; buvid3=56F7285C-5079-48AA-B620-3C094C471FEF190973infoc; LIVE_BUVID=AUTO1515697704665324; sid=m0a2veet; CURRENT_FNVAL=16; rpdid=|(JYYJJk~m|u0J'ulYm~~|YJJ; im_notify_type_68005955=0; UM_distinctid=16d90285550b59-0ca19d9a7fb011-67e1b3f-e1000-16d90285551b6f; stardustvideo=1; CURRENT_QUALITY=112; laboratory=1-1; DedeUserID=68005955; DedeUserID__ckMd5=51eeebfd2cc4a037; SESSDATA=e6663209%2C1581749930%2Ccd118d11; bili_jct=0936f83fb58346f1bf1520fd24c18611; stardustpgcv=0606; INTVER=1; bp_t_offset_68005955=346088752477987476"
    }
    data = {'type': '1','follow_status': '0','pn': page,'ps': '15','vmid': '68005955','ts': '1579443692587'}
    resp = requests.get(url,headers=header,params=data).text
    result = json.loads(resp)
    result_title = jsonpath(result,'$.data.list[*].title')
    result_evaluate = jsonpath(result,'$.data.list[*].evaluate')
    return result_title,result_evaluate
count = 1
for i in range(1,8):
    result_title,result_evaluate = bilibili_fav(i)
    fav = {}
    for k in range(len(result_evaluate)):
        result_evaluate[k] = repr(result_evaluate[k])
        result_evaluate[k] = result_evaluate[k].replace("\\n","")
    for i in range(len(result_title)):
        fav[result_title[i]] = result_evaluate[i]
    with open("bilibili_fav.txt","a+",encoding="utf-8") as f:
        for key in fav:
            f.write(str(count) + '.' + key + ":" + "\n" + fav[key] + "\n")
            count += 1