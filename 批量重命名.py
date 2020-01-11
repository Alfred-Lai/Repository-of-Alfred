#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
name_before = "18本科-商1-陈奕好,18本科-商1-李林杰,18本科-商1-吴泓瑾,18本科-商1-郑佳璿,18本科 - 商1 - 尹蔓莉,18本科-商1-杨书予,18本科-商1-朱云晓,18本科-商1-卿婷,18本科-商1-赵煜晨,18本科-商1-赵秀林,18本科-商1-刘若曦,18本科-商1-赖智彬,18本科-商1-华思民,18本科-商1-王文博,18本科-商1-张小凤,18本科-商1-欧洪缘,18本科-商1-陈卓,18本科-商1-潘俊容,18本科-商1-张雨菲,18本科-商1-魏胡玉,18本科-商1-曾薇,18本科-商1-余家慧,18本科-商1-金烨,18本科-商1-熊葆萱,18本科-商1-朱秋燕,18本科-商1-张馨怡,18本科-商1-王欣怡,18本科-商1-吴晓菁,18本科-商1-程子珈,18本科-商1-苏苗,18本科-商1-刘凯睿"
name_mid = name_before.split(",")
path = "C:\\Users\\Honor\\Desktop\\utf-8' '52820142_附件 - Copy"
file_name = os.listdir(path)
count = 0
for name in file_name:
    protion = os.path.splitext(path + file_name[count])
    protion = list(protion)
    new_name_protion = protion[1]
    new_name = name_mid[count] + new_name_protion
    os.rename(path + "\\" + name , path + "\\" + new_name)
    count += 1

