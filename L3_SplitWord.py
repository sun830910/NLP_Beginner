# -*- coding: utf-8 -*-

"""
Created on 12/8/20 1:50 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

"""
规则分词
"""


# 正向最大匹配算法
class MM(object):
    def __init__(self):
        self.window_size = 3

    def cut(self, text):
        result = []
        index = 0
        text_length = len(text)
        dict = ["研究", "研究生", "生命", "命", "的", "起源"]
        while index < text_length:
            for size in range(self.window_size + index, index, -1):
                piece = text[index:size]
                if piece in dict:
                    index = size - 1
                    break
            index += 1
            result.append(piece + '----')
        return result


class RMM(object):
    def __init__(self):
        self.window_size = 3

    def cut(self, text):
        result = []
        index = len(text)
        dict = ["研究", "研究生", "生命", "命", "的", "起源"]
        while index > 0:
            for size in range(index - self.window_size, index):
                piece = text[size:index]
                if piece in dict:
                    index = size + 1
                    break
            index -= 1
            result.append(piece + '----')
        result.reverse()
        return result


# 双向最大匹配
class biMM(object):
    def __init__(self):
        self.MM = MM()
        self.RMM = RMM()

    def cut(self, text):
        MMresult = self.MM.cut(text)
        RMMresult = self.RMM.cut(text)
        if len(MMresult) < len(RMMresult):
            return MMresult
        elif len(MMresult) > len(RMMresult):
            return RMMresult
        else:
            if (MMresult == RMMresult):
                return MMresult
            else:
                MMcnt = self.count(MMresult)
                RMMcnt = self.count(RMMresult)
                return MMresult if MMcnt > RMMcnt else RMMresult

    def count(self, arr):
        cnt = 0
        for idx in arr:
            if len(idx) == 1:
                cnt += 1
        return cnt


if __name__ == '__main__':
    text = "研究生命的起源"
    tokenizer = MM()
    print(tokenizer.cut(text))

    r_tokenizer = RMM()
    print(r_tokenizer.cut(text))

    bi_tokenizer = biMM()
    print(bi_tokenizer.cut(text))
