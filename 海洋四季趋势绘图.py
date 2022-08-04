import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy as cart
import matplotlib
from glob import glob
import os
font = {'family':'Times New Roman',
        'weight': 'semibold',
        'size': 11}
font2 = {'family':'Times New Roman',
        'weight': 'semibold',
        'size': 11}
matplotlib.rc("font", **font)

# ex_country_names = ('Antarctica','Greenland')

shp_file = shpreader.natural_earth(resolution='110m', category='cultural',name='admin_0_countries')


glass_file=r'F:\梁老师任务\四季\ocean_trend\ocean_winter_trend_land.npy'

glass_p=r'F:\梁老师任务\四季\ocean_trend\ocean_winter_p_rn_land.npy'

import cv2

glass_data=np.load(glass_file)

glass_data = cv2.resize(glass_data, (720, 360), interpolation=cv2.INTER_AREA)
lons=np.linspace(0,360,glass_data.shape[1])
lats=np.linspace(-90,90,glass_data.shape[0])[::-1]

fig = plt.figure(figsize=(10, 6))
ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.coastlines()
ax.set_xticks(np.linspace(-180, 180, 5), crs=ccrs.PlateCarree())
ax.set_yticks(np.linspace(-90, 90, 5), crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
clevs = np.linspace(-1.4,1.4, 20)
map_car=ax.contourf(lons, lats, glass_data,clevs,
            transform=ccrs.PlateCarree(),
            cmap=plt.cm.jet)
ax.add_feature(cart.feature.LAND, zorder=100, edgecolor='k', facecolor='w')

glass_pvalues=np.load(glass_p)
glass_pvalues = cv2.resize(glass_pvalues, (720, 360), interpolation=cv2.INTER_AREA)
for i in (range(glass_pvalues.shape[0])[::5]):
    for j in (range(glass_pvalues.shape[1])[::5]):
        if glass_pvalues[i,j]<0.05:
            ax.scatter(lons[j], lats[i], c='k', s=0.5, transform=ccrs.PlateCarree())

ax.set_title('Trend of Winter GLASS LHF',fontdict={'weight': 'bold', 'fontsize': 16})
ticks=np.linspace(-1.4,1.4,8)
cax = fig.add_axes([0.15, 0.04, 0.7, 0.03])
cbar=fig.colorbar(map_car, extend='both',
                shrink=1, ax=ax,ticks=ticks,cax=cax,orientation='horizontal')


ax.set_global()
fig.tight_layout()
plt.subplots_adjust(wspace =0, hspace =0)
plt.savefig(r'F:\梁老师任务\四季\ocean_trend\winter_sea.png')
plt.show()
