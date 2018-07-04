from rest_framework import serializers
from datetime import datetime, timedelta

from Notes.models import ShiYu
from .help_text import register_ecode_message,register_epwd_message
from django.contrib.auth import get_user_model

User = get_user_model()


class ShiYuSerializer(serializers.ModelSerializer):
    '''
    时域创建
    '''

    class Meta:
        model = ShiYu
        fields = ['title', 'desc', 'create_time', 'keep_time', 'image', ]


class KeySerializer(serializers.ModelSerializer):
    '''
    钥匙串查找
    '''

    class Meta:
        model = ShiYu
        fields = ['title', 'desc']


class UserRegisterSerializer(serializers.ModelSerializer):
    '''
    用户注册
    '''
    code = serializers.CharField(max_length=4, min_length=4, required=True,write_only=True,error_messages=register_ecode_message)
    r_password = serializers.CharField(max_length=12,min_length=3,required=True,write_only=True,error_messages=register_epwd_message)
    password = serializers.CharField(max_length=12,min_length=3,required=True,write_only=True,error_messages=register_epwd_message)
    username = serializers.CharField(required=False,allow_blank=True)
    #验证码处理
    def validate_code(self, code):
        # #验证验证码过期时间
        # one_min_ago = datetime.now() - timedelta(hours=0,minutes=5,seconds=0)
        s_code = self.context['request'].session.get('s_code', '')
        try:
            code = int(code)
        except Exception as e:
            raise serializers.ValidationError('验证码类型错误')
        if s_code != code:
            raise serializers.ValidationError('验证码不正确')

    # 字段处理
    def validate(self, attrs):
        if attrs['r_password'] != attrs['password']:
            raise serializers.ValidationError('两次输入密码不一致')
        attrs['username'] = attrs['email']
        del attrs['code']
        del attrs['r_password']
        return attrs

    def create(self, validated_data):
        user = super(UserRegisterSerializer,self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = [ 'username','email', 'password','r_password','code',]
