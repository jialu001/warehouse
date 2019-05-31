from django.db import models

# Create your models here.
class yi69(models.Model):
    changjia = models.CharField(max_length=50)
    mingcheng = models.CharField(max_length=100)
    xinghao = models.CharField(max_length=100)
    sn = models.CharField(max_length=100,null=True,blank=True)
    num = models.CharField(max_length=50,null=True,blank=True)
    place = models.CharField(max_length=50,null=True,blank=True)
    beizhu =  models.CharField(max_length=200,null=True,blank=True)
    gongcheng =  models.CharField(max_length=200,null=True,blank=True)
    zichanbiaoqian = models.CharField(max_length=50,null=True,blank=True)
    status =models.CharField(max_length=50,default="未出库")
