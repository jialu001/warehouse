from django.db import models

# Create your models here.
class guangMoKuai(models.Model):
    changjia = models.CharField(max_length=50)
    xinghao =  models.CharField(max_length=100)
    chengZaiWang =  models.IntegerField()
    chengYuWang = models.IntegerField()
    moveTo750 = models.IntegerField()
