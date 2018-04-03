from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)  #第一个参数不能和下面一个类里的外键一样加单引号，否则报错
                                                                #外键的第一个参数必须是一个model或者name of a model
    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)  #不加入参数二则会报错，指定外键的方式不对
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."