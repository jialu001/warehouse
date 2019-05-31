from django.db import models
from datetime import datetime
# Create your models here.
class cache(models.Model):
    op_user_name = models.CharField(max_length=50)
    op_type = models.CharField(max_length=50)
    op_item_id = models.CharField(max_length=50,default="")
    op_item = models.CharField(max_length=50)
    op_status =models.CharField(max_length=50)
    op_reason = models.CharField(max_length=100,default="")
    op_time = models.DateTimeField(default=datetime.now)
