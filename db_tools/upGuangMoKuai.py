import sys
import os
import pandas as pd
import numpy as np
import django
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append( "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "warehouse.settings")
django.setup()
from guangMoKuai.models import guangMoKuai


df = pd.read_excel('guangMoKuai.xlsx')



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
        if(str1 == "nan"):
            str1 = 0

        print(str1)
        if j == 0:
            changJia_r = str1
        if j == 1:
            xingHao_r = str1
        if j == 2:
            chengZaiWang_r =int(float(str1))
        if j == 3:
            chengYuWang_r = int(float(str1))
        if j == 4:
            moveTo750_r = int(float(str1))

    guangMoKuai.objects.create(changjia=changJia_r,xinghao=xingHao_r,chengZaiWang=chengZaiWang_r,chengYuWang=chengYuWang_r,moveTo750=moveTo750_r)


