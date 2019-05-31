from django.db import models

# Create your models here.
class guangMoKuai(models.Model):
    changjia = models.CharField(max_length=50)
    xinghao =  models.CharField(max_length=100)
    chengZaiWang =  models.IntegerField()
    chengYuWang = models.IntegerField()
    moveTo750 = models.IntegerField()
    change = models.IntegerField(default=0)

    # 0 --- init status 表示变化 ; 1表示 入库 中 ; 2表示 出库中 . 用于防止正在出库的GMK 又 入库 数量异常
    status = models.CharField(max_length=50,default="0")