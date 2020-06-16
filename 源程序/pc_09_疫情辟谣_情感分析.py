
from snownlp import SnowNLP
import pylab as pl
import pandas as pd

def createSnowNLO(path):
    txt = open(path, 'r', encoding='UTF-8')
    text = txt.readlines()
    txt.close()
    print('读入成功')
    sentences = []
    senti_score = []

    for i in text:
        a1 = SnowNLP(i)
        a2 = a1.sentiments
        sentences.append(i)  # 语序...
        senti_score.append(a2)
    table = pd.DataFrame(sentences, senti_score)

    pl.mpl.rcParams['font.sans-serif'] = ['SimHei']
    pl.figure(figsize=(50, 8))
    pl.plot(senti_score, linestyle='-')
    pl.title(u'疫情情感')
    pl.xlabel(u'疫情信息组')
    pl.ylabel(u'疫情程度')
    pl.show()

if __name__ == '__main__':
    path_txt = r'C:\Users\赵宗天\Desktop\认识Python\爬取文档\疫情辟谣2020-05-13-00-05_谣言_数据清洗.txt'
    createSnowNLO(path_txt)