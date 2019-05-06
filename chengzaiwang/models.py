from django.db import models

# Create your models here.
class chengzaiwang(models.Model):

    fengongsi = models.CharField(max_length=100,null=True,blank=True,verbose_name="分公司")

    name = models.CharField(max_length=100,null=True,blank=True,verbose_name="配件名称")

    xinghao = models.CharField(max_length=100,null=True,blank=True,verbose_name="规格型号")

    leixing = models.CharField(max_length=100,null=True,blank=True,verbose_name="类型")

    sn = models.CharField(max_length=100,null=True,blank=True,verbose_name="序列号")

    rukushijian = models.CharField(max_length=100,null=True,blank=True,verbose_name="入库时间")

    rukudidian = models.CharField(max_length=100,null=True,blank=True,verbose_name="入库地点")

    num = models.CharField(max_length=100,null=True,blank=True,verbose_name="数量")

    huoweihao = models.CharField(max_length=100,null=True,blank=True,verbose_name="货位号")

    dingdanhao = models.CharField(max_length=100,null=True,blank=True,verbose_name="订单号")

    diaochushijian = models.CharField(max_length=100,null=True,blank=True,verbose_name="调出时间")

    diaowangdi = models.CharField(max_length=100,null=True,blank=True,verbose_name="调往地")

    suoshuwangluo = models.CharField(max_length=100,null=True,blank=True,verbose_name="所属网络")

    beizhu = models.CharField(max_length=100,null=True,blank=True,verbose_name="备注")

    zichanbiaoqian = models.CharField(max_length=100,null=True,blank=True,verbose_name="资产标签")

    status = models.CharField(max_length=100,default="未出库")
    def __str__(self):

        if(self.name==None):
            return ""
        else:
            return self.name