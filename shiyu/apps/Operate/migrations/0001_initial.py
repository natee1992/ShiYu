# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-02 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_num', models.IntegerField(help_text='访问量')),
                ('register_num', models.IntegerField(help_text='点击注册页面量')),
                ('key_num', models.IntegerField(help_text='钥匙串页面访问量')),
                ('shiyu_num', models.IntegerField(help_text='时域存入访问量')),
            ],
            options={
                'verbose_name': '网站统计',
            },
        ),
    ]
