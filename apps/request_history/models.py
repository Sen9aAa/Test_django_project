from django.db import models

# Create your models here.
class RequestHistory(models.Model):
    request_method = models.CharField(max_length = 200)
    request_time = models.DateTimeField(auto_now_add = True)
    request_link = models.CharField(max_length = 200,blank = True,null = True)
    request_status = models.IntegerField(default = 0)