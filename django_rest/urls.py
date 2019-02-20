"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from joystick_api import views

#from joystick_api.views import hello_view
#from joystick_api.views import root_view
#from musics.views import hello_view
#from musics.views import root_view
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

#from musics import views



router = DefaultRouter()
router.register(r'User', views.APIViewSet)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('JAPI/', include(router.urls)),
    #path(''),
    path('/api-doc',include_docs_urls(title='JoyStick Applcation Backend',description="Test", public=True))
    #path('api/', include(router.urls))
]
