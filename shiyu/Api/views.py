from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ShiYuSerializer, KeySerializer, UserRegisterSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from Notes.models import ShiYu
from django.contrib.auth.models import User


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

