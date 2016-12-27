# -*- coding: utf-8 -*-
"""
使用非球形项目绘制中国地图：merc
方法：制定中国的左下角和右上角的经纬度
并且提高显示的精度：改变area_thresh，resolution

中国的大致经纬度范围_百度知道
答
最东端 东经135度2分30秒 黑龙江和乌苏里江交汇处
最西端 东经73度40分 帕米尔高原乌兹别里山口（乌恰县）
最南端 北纬3度52分 南沙群岛曾母暗沙
最北端 北纬53度33分 漠河以北黑龙江主航道（漠河)
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

plt.show()
