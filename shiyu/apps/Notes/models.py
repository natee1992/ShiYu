from datetime import datetime

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class ShiYu(models.Model):
    title = models.CharField(max_length=12, help_text='标题', default='未命名')
    desc = models.CharField(max_length=1024, help_text='时域内容')
    create_time = models.DateTimeField(default=datetime.now, help_text='创建时间')
    keep_time = models.DateTimeField(help_text='到期日期')
    user = models.ForeignKey(User)
    is_open = models.IntegerField(
        default=0, help_text='是否打开，默认0不为打开，1为打开（可扩展）')
    image = models.FileField(upload_to='upload/%Y/%m/%d',
                             help_text='记忆照片', null=True)
    open_code = models.CharField(
        default='', max_length=10, help_text='陌生人打开密码')
    is_send = models.IntegerField(default=0, help_text='是否发送即将到期提醒邮件')

    def random_str(self):
        abc_str = 'qwert!yuio@asdfghjkl#zxcvbnmQW$ERTYU%OPASDFGHJ&KLZXCVBNM0123456789'
        code = []
        while True:
            for i in range(14):
                r = random.choice(abc_str)
                code.append(r)
            code = ''.join(code)
            code_ = Note.objects.filter(open_code=code)
            if code_:
                return self.random_str()
            else:
                return code

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.open_code = self.random_str()
        super(Note, self).save(force_insert=False, force_update=False, using=None,
                               update_fields=None)

    class Meta:
        verbose_name = '时域库'
