import sys
import os
import pandas as pd
import numpy as np
import django
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "warehouse.settings")
django.setup()



df = pd.read_excel('ziyong.xlsx')

da= []

ziyong = 0
startip =""
for i in range((int(df.__len__()))):
    # 0 表示未知 1为自用
    #type = 0
    #存储该行IP
    ip = ""
    lastip = ""
    for j in range(int(df.columns.size)):
        cell = str(df.columns[j])
        str1 = (df[i:(i + 1)][cell].to_string())
        test = df[i:(i + 1)][cell].get_values()

        str1 = ((str)(test[0]))
        if(j==0):
            ip = str1
       #







        # info = str1.split('.')
        # print(info)
        #
        # for i in range(256):
        #     finINfo = str(i)
        #     str1 = info[0]+"."+info[1]+"."+info[2]+"."+finINfo
        #     da.append(str1)

#
# df1 = pd.DataFrame({'Data1':da})
#
# # create a Pandas Excel writer using xlswriter
# writer = pd.ExcelWriter('sj529.xlsx')
#
# df1.to_excel(writer, sheet_name='Data1', startcol=0, index=False)
#
# writer.save()

