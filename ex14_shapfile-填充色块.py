# -*- coding: utf-8 -*-
"""
认识shapefile功能
"""

from mpl_toolkits.basemap import shapefile, Basemap
import matplotlib.pyplot as plt
import time
from matplotlib.patches import PathPatch
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

# 构建地图实例
m = Basemap(projection='merc',
            llcrnrlon=73,
            llcrnrlat=15,
            urcrnrlon=135,
            urcrnrlat=55,
            resolution='c',
            lat_0=38.5,
            lon_0=95)

# 中国省份数据
filename = 'shapefiles/CHN_adm_shp/CHN_adm1'
# 使用shapefile读取文件，必须指定两个参数：路径和名字
# 但是不要加扩展名！
m.drawmapboundary()
m.fillcontinents(color='#78D2F9')
# m.drawcoastlines()
_info = m.readshapefile(filename, 'CHN_adm1', drawbounds=False)
print _info

patches = []

for info, shape in zip(m.CHN_adm1_info, m.CHN_adm1):

    if int(info['ID_1']):
        # 构建该省份的多边形，使用数据是一簇点
        # 必须使用np.array来传入参数
        # 下面的第二个参数 True表示：封闭图形
        # shape[::15]是为了少取一些点，提高效率
        patches.append(Polygon(np.array(shape[::15]), True))

# zorder=2 是说这个多边形在图形的第二层
ax.add_collection(PatchCollection(patches,
                  facecolor='#F78AE0',
                  edgecolor='k',
                  linewidth=.5,
                  zorder=2))

# # shapfile读取的文件是这个样子的：
# # 包含很多块数据
# print(len(m.CHN_adm1_info))
# # 每个省份一块
# print(m.CHN_adm1_info[0])
# # 每个省份区域由若干个点构成
# print(m.CHN_adm1[0])

plt.show()
# time.sleep(8)
# plt.delaxes()
