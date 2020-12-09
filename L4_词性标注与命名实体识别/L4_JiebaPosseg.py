# -*- coding: utf-8 -*-

"""
Created on 12/8/20 7:48 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""


import jieba.posseg as psg

sentence = "中文分词是文本处理不可或缺的一步"
seg_list = psg.cut(sentence)
print(''.join(['{0}/{1} '.format(w, t) for w, t in seg_list]))