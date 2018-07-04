from django.db import models

# Create your models here.


class CountNum(models.Model):
    v_num = models.IntegerField(help_text='访问量')
    register_num = models.IntegerField(help_text='点击注册页面量')
    key_num = models.IntegerField(help_text='钥匙串页面访问量')
    shiyu_num = models.IntegerField(help_text='时域存入访问量')

    def __str__(self):
        return self.v_num

    class Meta:
        verbose_name = '网站统计'

