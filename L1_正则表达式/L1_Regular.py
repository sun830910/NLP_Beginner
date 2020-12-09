# -*- coding: utf-8 -*-

"""
Created on 12/8/20 9:43 AM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import re


def sample1():
    text = "文本最重要的来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。利用一个爬虫抓取到网络中的信息。爬取的策略有广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。"
    splited = text.split("。")
    regex = "爬虫"
    for line in splited:
        if re.search(regex, line):
            print(line)


def sample2():
    text = "文本最重要的来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。利用一个爬虫抓取到网络中的信息。爬取的策略有广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。"
    splited = text.split("。")
    regex = "爬."
    for line in splited:
        if re.search(regex, line):
            print(line)


def sample3():
    text = "文本最重要的来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。利用一个爬虫抓取到网络中的信息。爬取的策略有广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。"
    splited = text.split("。")
    regex = "^文本"
    for line in splited:
        if re.search(regex, line):
            print(line)


def sample4():
    text = ['[重要的]今年第七号台风', '[紧要的]中国对印度']
    regex = "^\[[重紧]..\]"
    for line in text:
        if re.search(regex, line) is not None:
            print(line)
        else:
            print("No match")


if __name__ == '__main__':
    sample1()
    print("-" * 30)
    sample2()
    print("-" * 30)
    sample3()
    print("-" * 30)
    sample4()
