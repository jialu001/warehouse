from django.db import models

# Create your models here.

class operation(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=10)
    op_date = models.DateTimeField(auto_now=True)
    op_type = models.CharField(max_length=100)
    op_res = models.BooleanField()
    op_item = models.CharField(max_length=100)