# -*- coding: utf-8 -*-
"""
读取地震数据的经纬度，并画在图中
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import csv

# 获取地震数据的经纬度
lons, lats = [], []
filename = 'earthquake_20161220_1227.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        lats.append(float(row[1]))
        lons.append(float(row[2]))

print('lats:', lats[:5])
print('lons:', lons[:5])

# 构建map
m = Basemap(projection='robin',  # 项目
            lat_0=38.5,  # 中国为中心
            lon_0=95,
            resolution='c',  # 低解析度
            area_thresh=1000.0)  # 忽略小于1000平方千米的区域

m.drawcoastlines()  # 画海岸线
m.drawcountries()  # 画国家线
m.fillcontinents(color='#78D2F9')  # 填充大陆颜色
m.drawmapboundary()  # 投影区域边界--使图像更清晰
m.drawmeridians(np.arange(0, 360, 30), color='#666666')  # 经度
m.drawparallels(np.arange(-90, 90, 30), color='#666666')  # 维度

x, y = m(lons, lats)
m.plot(x, y, 'ro', markersize=6)
plt.show()
