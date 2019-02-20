from django.shortcuts import render
from joystick_api.models import User
from joystick_api.serializers import JAPI_Serializer
from rest_framework import viewsets, mixins

#from rest_framework import viewsets

# Create your views here.
class APIViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = JAPI_Serializer
