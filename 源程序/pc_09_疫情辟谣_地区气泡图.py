import numpy as np
from pyecharts import Geo

keys = ['湖北', '北京', '浙江', '上海', '黑龙江', '河北', '广东', '湖南', '河南', '山东', '重庆',
        '江苏', '广西', '安徽', '陕西', '江西', '吉林', '四川', '福建', '天津', '辽宁', '山西', '海南', '云南']
values = [83, 27, 24, 21, 21, 19, 19, 20, 11, 11, 9, 9, 7, 6, 6, 5, 5, 5, 5, 4, 4, 4, 2, 2]
test_geo = Geo("test", width=1200, height=600)
test_geo.use_theme('dark')

test_geo.add("气泡图", keys, values, maptype='china',
             is_visualmap=True,
             is_label_show=True,
             visual_type="size",
             border_color='#fff')  # 画地图散点十分建议指定边界颜色为一个较亮的颜色

test_geo  # notebook上会直接显示，不行就加上.render() 然后在当前文件目录上找
test_geo.render(path="C://Users//赵宗天//Desktop//认识Python//中国气泡图.html")
