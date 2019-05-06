from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True,verbose_name="姓名")
    # 权限等级
    level = models.IntegerField(default=0,verbose_name="权限等级")
    password = models.CharField(max_length=100,null=True,blank=True,verbose_name="密码")
    mobile = models.CharField(max_length=11,verbose_name="电话")
    email = models.CharField(max_length=100,null=True,blank=True,verbose_name="邮箱")

    class Meta:
        verbose_name ="用户"
        verbose_name_plural="用户"

    def __str__(self):

        if(self.name==None):
            return ""
        else:
            return self.name
