from django.db import models

class PersonData(models.Model):
    syskey = models.IntegerField(max_length=255, default=0)
    createdDate = models.CharField(max_length=255, default='')
    t1 = models.CharField(max_length=255, default='')
    t2 = models.CharField(max_length=255, default='')
    t5 = models.CharField(max_length=255, default='')
