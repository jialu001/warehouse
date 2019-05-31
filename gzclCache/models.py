from django.db import models
from datetime import datetime
# Create your models here.
class gzclcache(models.Model):
    username = models.CharField(max_length=100)
    chulididian = models.CharField(max_length=100)
    itemName = models.CharField(max_length=100)
    itemId   = models.CharField(max_length=50)
    itemNet  = models.CharField(max_length=100)
    op_time = models.DateTimeField(default=datetime.now)