import jieba.posseg as jp
import pyLDAvis.gensim
import pyLDAvis.sklearn
import umap
import matplotlib.pyplot as plt
from gensim import corpora, models
from gensim.models import word2vec

path = 'C://Users//赵宗天//Desktop//认识Python//爬取文档//'
flags = ['n', 'nr', 'ns', 'nt', 'eng', 'v', 'd']  # 词性
stopLists = ['谣言', '误区', '事实', '辟谣', '省', '市']  # 创建一个停用词列表
word_list = []


def ldaModel():
    # 停用词表
    with open(path + '停用词表.txt', 'r', encoding='utf-8') as f:
        for line in f:
            stopLists.append(line.strip())

    with open(path + '疫情辟谣2020-05-13-00-05_谣言_数据清洗2.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words = [w.word for w in jp.cut(line) if w.flag in flags and w.word not in stopLists]
            word_list.append(words)
    # 构造词典
    dictionary = corpora.Dictionary(word_list)
    # 基于词典，构造稀疏向量，放入列表形成稀疏向量集
    corpus = [dictionary.doc2bow(words) for words in word_list]
    # lda模型 num_topics=5主题个数
    lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5)
    for i in range(5):
        print('topic:' + str(i))
        print(print(lda.print_topic(i)))
    print(lda.inference(corpus))
    # pyLDAvis.save_html()
    vis = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
    pyLDAvis.show(vis)

    return word_list


def wordwvecModel():
    # 构建200个维度的模型
    model = word2vec.Word2Vec(word_list, size=200)
    # 获取词向量
    print(model.wv['新冠'])
    print(type(model.wv['新冠']))
    # 计算一个词的最近似的词，倒排序
    model.wv.most_similar(['新冠'])
    # 计算两个词之间的相似性以及和某个词相似性最高的词
    y2 = model.wv.similarity(u"新冠", u"病毒")
    print(y2)
    for i in model.wv.most_similar(u"新冠"):
        print(i[0], i[1])

    # 选出集合中不同类的词语
    list1 = ['恢复', '疫情', '快递', '开学', '上海', '物资', '吃']
    print(model.wv.doesnt_match(list1))

    # 用umap库进行可视化
    X = model[model.wv.vocab]
    # cluster_enbedding = umap.UMAP(n_neighbors=30, min_dist=0.0, n_components=2, random_state=42).fit_transform(X)
    cluster_enbedding = umap.UMAP(n_neighbors=30,
                                  min_dist=0.0,
                                  n_components=2,
                                  random_state=42).fit_transform(X)
    # 散点图
    plt.figure(figsize=(10, 9))
    plt.scatter(cluster_enbedding[:, 0], cluster_enbedding[:, 1], s=5, cmap='Spectral')
    plt.show()


if __name__ == '__main__':
    ldaModel()
    wordwvecModel()
