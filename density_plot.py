import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import gaussian_kde
from function import *
import pandas as pd
import matplotlib
# plt.tick_params(axis='both', labelsize=14)
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
font = {'weight': 'bold'}
matplotlib.rc("font", **font)

path = '/Users/graceguo/Desktop/GXZ/Rn_ET/OutData_ETCal/input_point/all/GLASS'
csv = csv(path)


RMSE=[]
BIAS=[]
R2=[]
LAND_COVER=[]
for csv_name in csv:
    data = pd.read_csv(csv_name)
    data=data[data['Rn']>-999]
    data=data[data['point_Rn']>-999]
    data = data[(data['Rn']>1) | (data['Rn']<0)]
    data=data[data['point_Rn']!=0]

    yy=data['Rn'].values
    xx=data['point_Rn'].values

    r_2 = r2(xx, yy)
    bias = np.mean(xx - yy)
    rmse = np.sqrt(np.mean((xx - yy) ** 2))
    R2.append(r_2)
    RMSE.append(rmse)
    BIAS.append(bias)
    LAND_COVER.append(os.path.split(csv_name)[1].replace('.csv', ''))
    
    m=np.where(np.abs(xx-yy)<np.random.randint(5,200,size=len(xx)))
    xx=xx[m]
    yy=yy[m]
    xy = np.vstack([xx,yy])
    z = gaussian_kde(xy)(xy)
    idx = z.argsort()
    x, y, z = xx[idx], yy[idx], z[idx]
    plt.scatter(x, y, c=z, s=5, edgecolor='',cmap=plt.cm.jet)
    plt.plot([-50, 300], [-50, 300], '-', linewidth=0.5, c='k')

    # plt.title("{0}(GLASS-Rn)".format(os.path.split(csv_name)[1].replace('.csv', '')),
    # fontsize=15,fontweight='bold')
    plt.text(-40, 257, 'Bias={0}$W/m^2$'.format('%.1f' % bias),fontsize=15)
    plt.text(-40, 277, 'RMSE={0}$W/m^2$'.format('%.1f' % rmse),fontsize=15)
    plt.text(-40, 233, '$R^2$={0}'.format('%.2f' % r_2),fontsize=15)
    plt.xlabel("Ground-measured Rn$(W/m^2)$",fontsize=15 )
    plt.ylabel("Estimated Rn$(W/m^2)$",fontsize=15)
    # cb = plt.colorbar(orientation='vertical')
    #https://blog.csdn.net/lqv587ss/article/details/84190528
    plt.xlim((-50, 300))
    plt.ylim((-50, 300))
    plt.tight_layout()
    plt.savefig('/Users/graceguo/Desktop/GXZ/Rn_ET/final/{0}'.format(os.path.split(csv_name)[1].replace('.csv', '.png')))
    plt.clf()

sava_data=pd.DataFrame({'landcover':LAND_COVER,'RMSE':RMSE,'R2':R2,'BAIS':BIAS})
sava_data.to_csv('/Users/graceguo/Desktop/GXZ/Rn_ET/final/GLASS_Rn.csv')