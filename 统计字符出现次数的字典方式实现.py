# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:52:04 2019

@author: 华为
"""
def count_str(sentence):
    count={}
    for word in sentence:
        if 'A' <= word <= 'Z' or 'a' <= word <= 'z':
            count[word] = count.get(word,0) + 1
    return count
a = "abcsadhwqidoqkasdsadwdqwfiqihahduqwidjqohqhfeq"
k = count_str(a)
print(list(k.items()))

