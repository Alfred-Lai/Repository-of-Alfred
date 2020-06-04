# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:36:10 2019

@author: 华为
"""
def averange_v(ls):
    ls_averange_v = []
    lenght = len(ls[0])
    for i in range(lenght):
        sum_mid = 0
        for k in ls:
            sum_mid += k[i]
        ls_averange_v.append(sum_mid / len(ls))
    return ls_averange_v
