from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=2)
    phone = models.CharField(max_length=11,null=True)
    email = models.EmailField(null=True)
    answer = models.CharField(max_length=50)
