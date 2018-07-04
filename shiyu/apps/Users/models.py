from datetime import datetime
import random

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(
        max_length=36, default='change_me', help_text='昵称')
    icon = models.CharField(max_length=128, help_text='头像')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = '用户信息表'


class Suggest(models.Model):
    connect = models.CharField(max_length=56, help_text='联系方式')
    tip = models.CharField(max_length=300, help_text='建议')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.tip

    class Meta:
        verbose_name = '网站建议'


class VerifyCode(models.Model):
    code = models.CharField(max_length=12,help_text='邮箱验证码')
    email = models.CharField(max_length=24,help_text='邮箱')
    add_time = models.DateTimeField(default=datetime.now,help_text='发送时间')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = '验证码'
