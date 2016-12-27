# -*- coding: utf-8 -*-
"""画一个国家地图-中国"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta


# 比较好看的中国地图
m = Basemap(width=5000000,
            height=4000000,
            projection='lcc',
            resolution='c',
            lat_1=3,
            lat_2=55,
            lat_0=37,
            lon_0=102)

# 画大陆边界线
m.drawcoastlines(color='k')
# 填充海洋颜色
m.drawmapboundary(fill_color='white')
# 填充大陆颜色
m.fillcontinents(color='white')
# 画国家线
m.drawcountries(color='k')
# 画state，对中国不起作用
m.drawstates()
# 画nightshade线，必须使用utc时间才准确
# m.nightshade((datetime.datetime.utcnow()-datetime.timedelta(hours=4)))
plt.show()



# # Basemap所有参数介绍
# m = Basemap(llcrnrlon=None,  #
#             llcrnrlat=None,  #
#             urcrnrlon=None,  #
#             urcrnrlat=None,  #
#             llcrnrx=None,  #
#             llcrnry=None,  #
#             urcrnrx=None,  #
#             urcrnry=None,  #
#             width=None,  #
#             height=None,  #
#             projection='cyl',  # 指定项目，默认是 cyl
#             resolution='c',  #
#             area_thresh=None,  #
#             rsphere=6370997.0,  #
#             ellps=None,  #
#             lat_ts=None,  #
#             lat_1=None,  #
#             lat_2=None,  #
#             lat_0=None,  #
#             lon_0=None,  #
#             lon_1=None,  #
#             lon_2=None,  #
#             o_lon_p=None,  #
#             o_lat_p=None,  #
#             k_0=None,  #
#             no_rot=False,  #
#             suppress_ticks=True,  #
#             satellite_height=35786000,  #
#             boundinglat=None,  #
#             fix_aspect=True,  #
#             anchor='C',  #
#             celestial=False,  #
#             round=False,  #
#             epsg=None,  #
#             ax=None)  #
