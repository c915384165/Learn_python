#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def getText(textName,  return_type='s', chName='en_signs.txt'):
    """打开一个纯文本文件，并替换掉符号，返回一个来字符串列表或空格分隔的长字符串，"""
    """
    输入:
        $1: 读取的文档
        $2: 输出的类型，s/string 字符串 l/list 列表
        $3: 用来替换成空格的标点, 默认打开 en_signs.txt
    输出:
        $2 来选择, 默认为字符串格式
        """
    txt = open(textName, 'r').read()  # 打开文档，读取数据到txt
    txt = txt.lower()  # 将txt中所有英文字符变成小写
    if chName != '':
        signs = open(chName, 'r').read()  # 导入标点文档，
        for ch in signs:
            txt = txt.replace(ch, " ")  # 用空格代替所有标点
    if return_type == "string" or return_type == "s":
        return txt
    elif return_type == "list" or return_type == "l":
        return txt.split()


"""
# 测试函数 getText
textName = 'hamlet.txt'
# chName = 'en_signs.txt'
# txt = getText(textName, chName, type='s')
# txt = getText(textName, chName, type='list')
txt = getText(textName, 'l')
print(txt)
print(len(txt))
"""


def count_words(words_list):
    """输入一个列表，统计列表中每个元素出现的频率
    ，并生成一个字典，以元素名为key，以出现次数为value"""
    counts = {}
    for word in words_list:
        counts[word] = counts.get(word, 0) + 1
    return counts


def rm_from_excludes(dic_name, excludes_file="excludes.txt"):
    """从字典中去掉 excludes文件包含的词"""
    excludes = getText(excludes_file, 'l')
    for word in excludes:
        del dic_name[word]


def dic_sort_ByValue(dic_name, reverse=False):
    """重新排序词典，按照词频出现的次数"""
    items = list(dic_name.items())
    items.sort(key=lambda x: x[1], reverse=reverse)
    return items


def print_topN(n, items):
    for i in range(n):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


"""
测试函数
"""


def main(textName, topN, reverse, chName='en_signs.txt', excludes_file="excludes.txt"):
    # 读取文档文件，返回列表，替换标点为空格，大写变小写
    txt = getText(textName, 'l', chName=chName)
    # 统计每个词出现的频率，返回词典，键为词，值为出现次数
    dcou = count_words(txt)
    # 去掉字典excludes文件中包含的词
    rm_from_excludes(dcou, excludes_file=excludes_file)
    # 排序生成顺序的列表, 字典类型是无法排序的，所以转化成列表
    dcou_list = dic_sort_ByValue(dcou, reverse=reverse)
    print_topN(topN, dcou_list)
    print("{} words.".format(len(txt)))
    print("{} non repeat words.".format(len(dcou_list)))

textName = 'hamlet.txt'
main(textName, 3, reverse=True)
