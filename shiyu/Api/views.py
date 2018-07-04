from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ShiYuSerializer, KeySerializer, UserRegisterSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from Notes.models import ShiYu
from django.contrib.auth.models import User
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler


class ShiYuViewSets(CreateModelMixin, viewsets.GenericViewSet):
    queryset = ShiYu.objects.all()
    serializer_class = ShiYuSerializer


class KeyViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = ShiYu.objects.all()
    serializer_class = KeySerializer


class UserViewsets(CreateModelMixin, viewsets.GenericViewSet):
    '''
    用户
    '''
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #生成token
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

