from pyecharts import Geo

keys = ['湖北', '北京', '浙江', '上海', '黑龙江', '河北', '广东', '湖南', '河南', '山东', '重庆',
        '江苏', '广西', '安徽', '陕西', '江西', '吉林', '四川', '福建', '天津', '辽宁', '山西', '海南', '云南']
values = [83, 27, 24, 21, 21, 19, 19, 20, 11, 11, 9, 9, 7, 6, 6, 5, 5, 5, 5, 4, 4, 4, 2, 2]

geo = Geo("全国主要城市辟谣热力图", "data from rumour", title_color="#fff", title_pos="left", width=1200, height=600,
          background_color='#404a59')

geo.add("谣言数量热力图", keys, values, visual_range=[0, 90], type='effectScatter', visual_text_color="#fff", symbol_size=15,
        is_visualmap=True, is_roam=True)
# type有scatter, effectScatter, heatmap三种模式可选，可根据自己的需求选择对应的图表模式
geo.render(path="C://Users//赵宗天//Desktop//认识Python//中国地图.html")
