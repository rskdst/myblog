from django.db import models
from datetime import datetime
from Userinfo.models import UserInfo
# Create your models here.
class UserMessage(models.Model):
    message_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(to="self",on_delete=models.CASCADE,related_name="parents_id",null=True)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    reply = models.ForeignKey(to="self",on_delete=models.CASCADE,related_name="reply_to",null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


