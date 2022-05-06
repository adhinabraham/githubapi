from http.client import HTTPResponse
import string
from django.shortcuts import render
import requests
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import json

# Create your views here.
class github(APIView):
       
    def post (self,request):
        forksnumber=request.data['forks']
        self.github_url = r'https://api.github.com/'
        print('thisi api view ')
        url=f'https://api.github.com/search/repositories?q=forks:>{forksnumber}+sort:forks-desc'
        githubdata=requests.get(url)
        content=githubdata
        print(content)
        return Response ({"content":content} )

# {"forks":"8"}
# https://api.github.com/search/repositories?q=forks:%3C50+sort:forks-desc
