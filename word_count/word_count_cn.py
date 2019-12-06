#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 问题1 同义词处理
# lcut 的返回结果
import jieba


def getText_cn(textName, chName='cn_signs.txt'):
    txt = open(textName, 'r', encoding='utf-8').read()  # 打开文档，读取数据到txt
    if chName != '':
    	signs = open(chName, 'r').read()
    	for ch in signs:
    		txt = txt.replace(ch, ' ')
    return jieba.lcut(txt)


path = "/Users/mac/learn/python3/word_count/"
textName = 'threekingdoms.txt'
chName = 'cn_signs.txt'
textName = path + textName
chName = path + chName
print(textName)
txt = getText_cn(textName)
print(txt)
"""
print(inputtxt)
"""
