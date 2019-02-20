from django.shortcuts import render
from joystick_api.models import User
from joystick_api.serializers import JAPI_Serializer
from rest_framework import viewsets, mixins

#from rest_framework import viewsets
#mixins.UpdateModelMixin
# Create your views here.
class APIViewSet(viewsets.ModelViewSet):
    """
    HJUAV Applcation backend
    """
    queryset = User.objects.all()
    serializer_class = JAPI_Serializer
    http_method_names = ['get','post']
