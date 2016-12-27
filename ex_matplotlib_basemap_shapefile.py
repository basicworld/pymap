from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(width=5000000,
            height=4000000,
            projection='lcc',
            resolution='c',
            lat_1=3,
            lat_2=55,
            lat_0=37,
            lon_0=102)

map.drawmapboundary(fill_color='white')
map.fillcontinents(color='#dddddd',lake_color='white')
map.drawcoastlines()

map.readshapefile('CHN_adm_shp/CHN_adm1','CHN_adm1')

plt.show()
