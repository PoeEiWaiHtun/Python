from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PersonData:
    # syskey = models.IntegerField(max_length=255, default=0)
    # createdDate = models.CharField(max_length=255, default='')
    # t1 = models.CharField(max_length=255, default='')
    # t2 = models.CharField(max_length=255, default='')
    # t5 = models.CharField(max_length=255, default='')

    syskey : int
    createdDate: str
    t1: str
    t2: str
    t5: str



