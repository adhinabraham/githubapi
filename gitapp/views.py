from http.client import HTTPResponse
from django.shortcuts import render
import requests
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import json

# Create your views here.
class github(APIView):
    def get (self,request):
        print('thisi api view ')
        githubdata=requests.get('https://api.github.com/users')
        content=githubdata
        print(content)
        return Response ({"content":content} )



