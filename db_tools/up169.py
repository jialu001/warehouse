import sys
import os
import pandas as pd
import numpy as np
import django
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "warehouse.settings")
django.setup()
from yi69.models import yi69


df = pd.read_excel('169.xlsx')



for i in range((int(df.__len__()))):
    for j in range(int(df.columns.size)):
        cell = str(df.columns[j])
        str1 = (df[i:(i + 1)][cell].to_string())
        test = df[i:(i + 1)][cell].get_values()
        if (type(test[0]) == np.datetime64):
            str1 = (str)(test[0])[:10]
            print(str1)
        else:
            str1 = ((str)(test[0]))


        print(str1)
        if j == 0:
            changJia_r = str1
        if j == 1:
            mingcheng_r = str1
        if j == 2:
            xinghao_r =str1
        if j == 3:
            sn_r = str1
        if j == 4:
            num_r =str1
        if j == 5:
            place_r = str1
        if j == 6:
            beizhu_r = str1
        if j == 7:
            gongcheng_r = str1
        if j == 8:
            zichanbiaoqian_r = str1
    yi69.objects.create(changjia=changJia_r,mingcheng=mingcheng_r, \
                        xinghao=xinghao_r,sn=sn_r,num=num_r, \
                        place=place_r,beizhu=beizhu_r,gongcheng=gongcheng_r,\
                        zichanbiaoqian=zichanbiaoqian_r)


