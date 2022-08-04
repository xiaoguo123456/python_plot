import statsmodels.api as sm
import numpy as np
import random
import os
from osgeo import gdal,osr
from tqdm import tqdm

def cal_trend(dict_data):
    if len(dict_data.keys()) > 5:

        X = sm.add_constant(list(dict_data.keys()))

        model = sm.OLS(list(dict_data.values()), X)
        results = model.fit()

        return results.params[1], results.pvalues[0]
    else:
        return np.nan


path = r'E:\BaiduNetdiskDownload\ET_0.5D\四季\modis'

# data = []
# date = range(2000, 2019)
#
# for i in date:
#     s_data=gdal.Open(os.path.join(path, str(i)+'_Autumn' + '.tif')).ReadAsArray()/100
#     s_data=np.where(np.abs(s_data)<0.000001,0,s_data)
#     data.append(s_data)
# data = np.array(data)
# Trendarray = np.zeros((data.shape[1], data.shape[2])).astype(np.float)
# parray = np.zeros((data.shape[1], data.shape[2])).astype(np.float)
# for i in tqdm(range(data.shape[1])):
#     for j in range(data.shape[2]):
#         # 提取像元值
#         all_pixel = {date[k]: data[k, i, j] for k in range(19)}
#         # 去除空值
#         all_pixel = {k[0]: k[1] for k in all_pixel.items() if not np.isnan(k[1])}
#
#         Trendarray[i, j] = cal_trend(all_pixel)[0]
#         parray[i, j] = cal_trend(all_pixel)[1]
#
# np.save(r'F:\梁老师任务\四季\AVHRR_TREND\AVHRR_Autumn_trend_land.npy', Trendarray)
# np.save(r'F:\梁老师任务\四季\AVHRR_TREND\\AVHRR_Autumn_p_rn_land.npy', parray)
#
#
#
# data = []
# date = range(2000, 2019)
#
# for i in date:
#     s_data=gdal.Open(os.path.join(path, str(i)+'_winter' + '.tif')).ReadAsArray()/100
#     s_data=np.where(np.abs(s_data)<0.000001,0,s_data)
#     data.append(s_data)
# data = np.array(data)
# Trendarray = np.zeros((data.shape[1], data.shape[2])).astype(np.float)
# parray = np.zeros((data.shape[1], data.shape[2])).astype(np.float)
# for i in tqdm(range(data.shape[1])):
#     for j in range(data.shape[2]):
#         # 提取像元值
#         all_pixel = {date[k]: data[k, i, j] for k in range(19)}
#         # 去除空值
#         all_pixel = {k[0]: k[1] for k in all_pixel.items() if not np.isnan(k[1])}
#
#         Trendarray[i, j] = cal_trend(all_pixel)[0]
#         parray[i, j] = cal_trend(all_pixel)[1]
#
# np.save(r'F:\梁老师任务\四季\AVHRR_TREND\AVHRR_winter_trend_land.npy', Trendarray)
# np.save(r'F:\梁老师任务\四季\AVHRR_TREND\\AVHRR_winter_p_rn_land.npy', parray)



data = []
date = range(2000, 2019)

for i in date:
    s_data=gdal.Open(os.path.join(path, str(i)+'_spring' + '.tif')).ReadAsArray()/100
    s_data=np.where(np.abs(s_data)<0.000001,0,s_data)
    data.append(s_data)
data = np.array(data)
Trendarray = np.zeros((data.shape[1], data.shape[2])).astype(np.float)
parray = np.zeros((data.shape[1], data.shape[2])).astype(np.float)
for i in tqdm(range(data.shape[1])):
    for j in range(data.shape[2]):
        # 提取像元值
        all_pixel = {date[k]: data[k, i, j] for k in range(19)}
        # 去除空值
        all_pixel = {k[0]: k[1] for k in all_pixel.items() if not np.isnan(k[1])}

        Trendarray[i, j] = cal_trend(all_pixel)[0]
        parray[i, j] = cal_trend(all_pixel)[1]

np.save(r'F:\梁老师任务\四季\AVHRR_TREND\AVHRR_spring_trend_land.npy', Trendarray)
np.save(r'F:\梁老师任务\四季\AVHRR_TREND\\AVHRR_spring_p_rn_land.npy', parray)



data = []
date = range(2000, 2019)

for i in date:
    s_data=gdal.Open(os.path.join(path, str(i)+'_summer' + '.tif')).ReadAsArray()/100
    s_data=np.where(np.abs(s_data)<0.000001,0,s_data)
    data.append(s_data)
data = np.array(data)
Trendarray = np.zeros((data.shape[1], data.shape[2])).astype(np.float)
parray = np.zeros((data.shape[1], data.shape[2])).astype(np.float)
for i in tqdm(range(data.shape[1])):
    for j in range(data.shape[2]):
        # 提取像元值
        all_pixel = {date[k]: data[k, i, j] for k in range(19)}
        # 去除空值
        all_pixel = {k[0]: k[1] for k in all_pixel.items() if not np.isnan(k[1])}

        Trendarray[i, j] = cal_trend(all_pixel)[0]
        parray[i, j] = cal_trend(all_pixel)[1]

np.save(r'F:\梁老师任务\四季\AVHRR_TREND\AVHRR_summer_trend_land.npy', Trendarray)
np.save(r'F:\梁老师任务\四季\AVHRR_TREND\\AVHRR_summer_p_rn_land.npy', parray)