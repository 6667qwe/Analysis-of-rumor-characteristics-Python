import xlrd
import pylab as pl
import pandas as pd

path = 'C://Users//赵宗天//Desktop//认识Python//爬取文档//'
file1 = '疫情辟谣2020-06-02-00-05_事实_日期_降序分类汇总.xlsx'
old_file = path + file1

date = []
data = []
date_data = {}


def getSum():
    rbook = xlrd.open_workbook(old_file)
    rbook.sheets()
    rsheet = rbook.sheet_by_index(0)
    for row in rsheet.get_rows():
        date_column = row[4]
        date_value = date_column.value
        if date_value != '' and date_value != '总计数':
            data_column = row[5]
            data_value = data_column.value

            s_date = date_value.split()[0]  # 去掉计数二字
            date.append(s_date)
            data.append(data_value)
    date.reverse()
    data.reverse()


    table = pd.DataFrame(date, data)
    pl.mpl.rcParams['font.sans-serif'] = ['SimHei']
    x = date
    y = data

    pl.figure(figsize=(15,5))
    pl.xticks(size='small', rotation=68)
    pl.plot(x, y, 'ob-', label=u'疫情事实新闻日增时间变化图')  # 'ob'带结点
    pl.title(u'疫情事实新闻日增数量')
    pl.xlabel(u'日期')
    pl.ylabel(u'数量')
    pl.show()

if __name__ == '__main__':
    getSum()
