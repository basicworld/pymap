# -*- coding: utf-8 -*-
"""
让地图更漂亮
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import csv


# 获取地震数据的经纬度
lons, lats = [], []
mags = []
times = []
filename = 'earthquake_20161220_1227.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        lats.append(float(row[1]))
        lons.append(float(row[2]))
        mags.append(float(row[4]))
        times.append(row[12])

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
# m.fillcontinents(color='#78D2F9')  # 填充大陆颜色
m.bluemarble()  # 显示真实地理图形
m.drawmapboundary()  # 投影区域边界--使图像更清晰
m.drawmeridians(np.arange(0, 360, 30), color='#666666')  # 经度
m.drawparallels(np.arange(-90, 90, 30), color='#666666')  # 维度

# 颜色标注函数
max_mag, min_mag = max(mags), min(mags)
def get_red_color(magnitude, max_mag=max_mag, min_mag=min_mag):
    """返回红色的渐变色"""
    scale = max_mag - min_mag
    c = (max_mag - magnitude) / float(scale)
    return (1, c, c)  # rgb颜色

mag_scalar = 2.5
x, y = m(lons, lats)
for x, y, mag in zip(x, y, mags):
    m.plot(x, y, 'o', color=get_red_color(mag), markersize=mag*mag_scalar)

title = u'全球地震数据检测图(1.0级以上)\n'
title += u"(%s ~ %s)" % (min(times), max(times))
plt.title(title)

plt.show()
