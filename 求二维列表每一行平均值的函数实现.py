# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:35:36 2019

@author: 华为
"""
def averange_h(ls):
    ls_average_h = []
    for i in ls:
        sum_mid = 0
        for k in i:
            sum_mid += k
        ls_average_h.append(sum_mid / len(i))
    return ls_average_h
