import os
import re
import jieba
import xlrd
from openpyxl import Workbook

path = 'C://Users//赵宗天//Desktop//认识Python//爬取文档//'
file = '疫情辟谣2020-06-02-00-05_事实.xlsx'
oldfile = path + file
news_list = []  # 创建一个列表封装文本内容
stopList = ['谣言', '误区', '事实', '辟谣', '省', '市']  # 创建一个停用词列表

cut_file = path + '疫情辟谣2020-06-02-00-05_事实_数据清洗.txt'


def dataClean():

    with open(path + '停用词表.txt', 'r', encoding='utf-8') as f:
        for line in f:
            stopList.append(line.strip())
    rbook = xlrd.open_workbook(oldfile)
    rbook.sheets()
    rsheet = rbook.sheet_by_index(0)  # 取第一个工作簿
    # 循环工作簿的所有行
    for row in rsheet.get_rows():
        date_column = row[0]  # 品名所在的列
        date_value = date_column.value  # 项目名
        if date_value != '标题':  # 排除第一行
            news_column = row[0]
            news_value = news_column.value
            news_list.append(news_value)
    # print(url_list)

    # 循环对列表中的内容进行清洗
    for i in range(len(news_list)):
        text0 = news_list[i]  # 获取文本内容
        text1 = re.sub("@([\s\S]*?):", "", text0)  # 去@
        text2 = re.sub("\[([\S\s]*?)\]", "", text1)  # ...]:
        text3 = re.sub("@([\s\S]*?)", "", text2)  # 去@...
        text4 = re.sub("[\.\!\/_,$%^*(+\"\']+|[+——! ，。？、~@#￥%&* （） ]+", "", text3)  # 去除标点及特殊符号
        # text5 = re.sub("[^\u4e00-\u9fa5]", "", text4)  # 去除所有非汉字内容(英文数字)
        new_text = jieba.cut(text4, cut_all=False)  # 精确模式
        # 此处生成的结果是"迭代器"。可以用循环打开，还可以用" ".join()的方式打开
        # str_out = ' '.join(new_text)

        # 输出结果为outstr
        outstr = ''
        # 去停用词
        for word in new_text:
            if word not in stopList:
                if word != '\t':
                    outstr += word
                    outstr += " "
            end_text = ''.join(outstr)
        news_list[i] = end_text
    # 去除生成的空行
    for j in news_list:
        if j == '':
            news_list.remove(j)
    # 写入文件
    wb2 = Workbook()
    if not os.path.exists(path):
        os.mkdir(path)
    wb2.save(filename=cut_file)
    fo = open(cut_file, 'w', encoding='utf-8')
    for i in range(len(news_list)):
        fo.write(news_list[i] + '\n')  # 换行写入，一个元素一行
        print(news_list[i])
    fo.close()
    print("文件保存成功")



if __name__ == '__main__':
    dataClean()
