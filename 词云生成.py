#!/usr/bin/python
# -*- coding: utf-8 -*-
import jieba
import wordcloud
#定义词云生成函数，变量为分割好的词语列表
def make_wordcloud(text):
    text = jieba.lcut(text)
    text = " ".join(text)
    w = wordcloud.WordCloud(
        background_color= 'white',
        max_words= 50,
        font_path= "楷体_GB2312.ttf",
        ).generate(text)
    w.to_file("name.png")

#定义将读取的每一行提取信息并转换为字符串的函数
'''def transfer(flie_in_line):
    file_dic = eval(flie_in_line)
    title_name = file_dic['title']
    return title_name
'''
#读取文本类容
f = open("2020新年贺词.txt","r",encoding="utf-8")
name_str = str(f.readlines())

#反复读取每一行标题，形成文本
'''with open("清华新闻爬取.txt","r",encoding="utf-8") as f:
    for line in f:
        name_str = name_str + transfer(line) + ','
'''

make_wordcloud(name_str)