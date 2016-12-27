# -*- coding: utf-8 -*-
"""
标注北京坐标
北京市区坐标为：北纬39.9”，东经116. 3”。
香港位于中国大陆南部,在北纬22.5度,东经114度
上海市地处东经121,北纬31

标注文字
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

m = Basemap(projection='merc',  # 项目
            lat_0=38.5,  # 中国为中心
            lon_0=95,
            resolution='c',  # 低解析度
            area_thresh=1000.0,  # 忽略小于1000平方千米的区域
            llcrnrlon=73,
            llcrnrlat=4,
            urcrnrlon=135,
            urcrnrlat=55)

m.drawcoastlines()  # 画海岸线
m.drawcountries()  # 画国家线
m.fillcontinents(color='#78D2F9')  # 填充大陆颜色
m.drawmapboundary()  # 投影区域边界--使图像更清晰
m.drawmeridians(np.arange(0, 360, 30), color='#666666')  # 经度
m.drawparallels(np.arange(-90, 90, 30), color='#666666')  # 维度

lons = [116.3, 114, 121]
lats = [39.9, 22.5, 31]
x, y = m(lons, lats)  # 将经纬度转换为特定项目的横纵坐标轴
m.plot(x, y, 'ro', markersize=10)  # 把点画在图上, ro:红色的圈

# 标注文字
labels = [u'北京', u'香港', u'上海']
for l, xi, yi in zip(labels, x, y):
    plt.text(xi*1.03, yi*0.98, l)  # 有两个系数是为了防止文字覆盖图形

plt.show()
