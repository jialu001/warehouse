from django.db import models
from datetime import datetime
# Create your models here.
class ywktcache(models.Model):
    username = models.CharField(max_length=100)
    diaodanHao = models.CharField(max_length=100)
    ToItemName = models.CharField(max_length=100)
    ToItemSlot = models.CharField(max_length=50)
    itemName = models.CharField(max_length=100)
    itemId   = models.CharField(max_length=50)
    itemNet  = models.CharField(max_length=100)
    op_time = models.DateTimeField(default=datetime.now)
