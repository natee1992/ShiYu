# '2018/7/4 16:40'
from django.shortcuts import render
from django.views.generic.base import View


class UserView(View):
    def get(self,request):
        return render(request,'index.html',{})
