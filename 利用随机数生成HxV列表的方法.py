# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:50:04 2019

@author: 华为
"""
import random
def creat_list(h,v,a,b):
    ls_all=[]
    ls_mid=[]
    for i in range(v*h):
        ls_mid.append(random.randint(a,b))
        if len(ls_mid) == h:
            ls_all.append(ls_mid.copy())
            ls_mid.clear()
    return ls_all
print(creat_list(5,4,1,10))