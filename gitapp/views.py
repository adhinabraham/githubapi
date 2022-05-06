from datetime import date
from http.client import HTTPResponse
from multiprocessing import context
import string
from django.shortcuts import render
import requests
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json
import io

# Create your views here.
class github(APIView):
   
    def post (self,request):
        forksnumber=request.data['forks']
        
        
        url=f'https://api.github.com/search/repositories?q=forks:>{forksnumber}+sort:forks-desc'
        githubdata=json.loads((requests.get(url).text))
        reporesults = []
        for repo in githubdata['items'][:1]:
            print(repo['id'])
            reporesults.append([repo['id'],repo['name'],repo['forks'], repo['commits_url'][:-6]])
        
        for commits in reporesults[:1]:
            print(commits[-1],"commits")
        
            commit_urls=commits[-1]
            commit_data=json.loads((requests.get(commit_urls).text))
           
            personlist=[]
            commitcount=[]
            
        
            for person in commit_data:
                if person['committer']['id'] in personlist:
    
                    index = personlist.index(person['committer']['id'])
                    
                    count = commitcount[index] +1
                               
                    commitcount[index]=count
                else:
                   
                    personlist.append(person['committer']['id'])
                    commitcount.append(1)
            
                
            result = [[person['committer']['id'] for person in commit_data] ]
            
            
            print("Committee ID", personlist)
            print("Committee count", commitcount)
            context={"largest_no_of_fork_repo":reporesults,"Committee ID": personlist,"Committee count": commitcount}

   

        return Response ({"message":"success", "data":context})


    
# {"forks":"8"}
# https://api.github.com/search/repositories?q=forks:%3C50+sort:forks-desc
