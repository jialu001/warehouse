import sys
import os
import pandas as pd
import numpy as np

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "warehouse.settings")

import django

django.setup()
from chengzaiwang.models import chengzaiwang


df = pd.read_excel('2019031302.xlsx')



for i in range((int(df.__len__()))):
    for j in range(int(df.columns.size)):
        cell = str(df.columns[j])
        str1 = (df[i:(i + 1)][cell].to_string())
        test = df[i:(i + 1)][cell].get_values()
        #时间格式的时候 只取前40
        if (type(test[0]) == np.datetime64):
            str1 = (str)(test[0])[:10]
            print(str1)
        else:
            str1 = ((str)(test[0]))
        print(str1)
        if j == 0:
            fengongsi_r = str1
        if j == 1:
            name_r = str1
        if j == 2:
            xinghao_r = str1
        if j == 3:
            leixing_r = str1
        if j == 4:
            sn_r = str1
        if j == 5:

            rukushijian_r = str1
        if j == 6:
            rukudidian_r = str1
        if j == 7:
            num_r = str1
        if j == 8:
            huoweihao_r = str1
        if j == 9:
            dingdanhao_r = str1
        if j == 10:
            diaochushijian_r = str1
        if j == 11:
            diaowangdi_r = str1
        if j == 12:
            suoshuwangluo_r = str1
        if j == 13:
            beizhu_r = str1
        if j == 14:
            zichanbiaoqian_r = str1

    chengzaiwang.objects.create(fengongsi=fengongsi_r,name=name_r,xinghao=xinghao_r,leixing=leixing_r,sn=sn_r,rukushijian=rukushijian_r,rukudidian=rukudidian_r,num=num_r,huoweihao=huoweihao_r,dingdanhao=dingdanhao_r,diaochushijian=diaochushijian_r,diaowangdi=diaowangdi_r,suoshuwangluo=suoshuwangluo_r,beizhu=beizhu_r,zichanbiaoqian=zichanbiaoqian_r
                                )
