# -*- coding: utf-8 -*-

"""
Created on 12/8/20 6:18 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

import jieba


def sample():
    sentence = "中文分词是文本处理不可或缺的一步"
    seg_list = jieba.cut(sentence, cut_all=True)
    print("全模式:", '/'.join(seg_list))

    seg_list = jieba.cut(sentence, cut_all=False)
    print("精确模式:", '/'.join(seg_list))

    seg_list = jieba.cut(sentence)
    print("默认精确模式:", '/'.join(seg_list))

    seg_list = jieba.cut_for_search(sentence)
    print("搜索引擎模式:", '/'.join(seg_list))


def get_content(path):
    with open(path, 'r', encoding='gbk', errors='ignore') as f:
        content = ''
        for l in f:
            l = l.strip()
            content += l
        return content


def get_TF(words, topK=10):
    tf_dic = {}
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0) + 1
    return sorted(tf_dic.items(), key=lambda x: x[1], reverse=True)[:topK]


def stop_words(path):
    with open(path) as f:
        return [l.strip() for l in f]


if __name__ == '__main__':
    stop_words('./data/L3/stop_words.utf8')
    import glob
    import random
    import jieba

    files = glob.glob('./data/L3/news/C000013/*.txt')
    corpus = [get_content(x) for x in files[:5]]

    sample_inx = random.randint(0, len(corpus))
    sample_inx = 3

    import jieba.posseg as psg

    split_words = [x for x in jieba.cut(corpus[sample_inx]) if x not in stop_words('./data/L3/stop_words.utf8')]
    print('样本之一：' + corpus[sample_inx])
    print('样本分词效果：' + '/ '.join(split_words))
    print('样本的topK（10）词：' + str(get_TF(split_words)))
