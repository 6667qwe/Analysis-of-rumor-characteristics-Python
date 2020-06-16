# -*- coding: UTF-8 -*-
import jieba
import re
from pyhanlp import *

path_txt = 'C://Users//赵宗天//Desktop//认识Python//爬取文档//疫情辟谣2020-05-13-00-05_谣言_数据清洗2.txt'
txt = open(path_txt, "r", encoding="utf-8").read()

words = jieba.lcut(txt)
counts = {}
place_list = []
featword= []

pos_list = ['nr', 'ns', 'nt', 'nz']  # 人名，地名，机构名，其他
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

# print(items[0][0])
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:<5}".format(word, count))

'''
for i in range(len(items)):
    CRFnewSegment = HanLP.newSegment('crf')
    term = CRFnewSegment.seg(items[i][0])

    ns = re.compile(r'ns')
    macth = ns.findall(str(term[0]))
    if macth:
        if items[i][1] > 1:
            print(items[i])
            place_list.append(items[i])
print(place_list)


CRFnewSegment = HanLP.newSegment('crf')
term = CRFnewSegment.seg('武汉')
# print(term)
'''


# print(featword)



