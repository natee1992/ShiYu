"""shiyu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from Api.urls import router
from Users.views import CodeView


from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='restframework')),
    # url(r'^api-token-auth/', views.obtain_auth_token),
    #jwt的认证接口
    url(r'^login/', obtain_jwt_token),
    url(r'^code/',CodeView.as_view()),
#-----------------------------------------------------------------------------------
    url(r'',TemplateView.as_view(template_name='index.html'),name='index'),
    url(r'search/',TemplateView.as_view(template_name='search.html'),name='search'),
    url(r'userinfo/',TemplateView.as_view(template_name='userinfo.html'),name='userinfo'),
]
