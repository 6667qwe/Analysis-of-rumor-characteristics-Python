import matplotlib.pyplot as plt
from wordcloud import WordCloud


def createWordcloud(path):
    # 打开content.txt文件，并将编码设为utf-8
    f = open(path, 'r', encoding='utf-8').read()
    # print(f)
    wc = WordCloud(
        # 设置字体
        font_path='C://Windows//Fonts//msyh.ttc',
        # 设置背景
        background_color="white", width=3000, height=2500).generate(f)

    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    wc.to_file('C://Users//赵宗天//Desktop//认识Python//词云图//疫情辟谣2020-05-13-00-05_谣言_数据清洗2.jpg')
    plt.show()


if __name__ == '__main__':
    # 要读取的文件
    path_txt = 'C://Users//赵宗天//Desktop//认识Python//爬取文档//疫情辟谣2020-05-13-00-05_谣言_数据清洗2.txt'
    createWordcloud(path_txt)
