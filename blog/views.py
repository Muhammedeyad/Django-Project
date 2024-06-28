from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from blog.models import post
from django.http import Http404
# appName = [
#         {'id':1, 'names': 'post1', 'content': 'viewing post one'},
#         {'id':2, 'names': 'post2', 'content': 'viewing post two'},
#         {'id':3,'names': 'post3', 'content': 'viewing post three'},
#         {'id':4, 'names': 'post4', 'content': 'viewing post four'},
        
#     ]

# Create your views here.
def index(request):
    appName = post.objects.all()
    return render(request, 'index.html', {"postItem": appName})

def detail(request, post_id):
    try:
        items = post.objects.get(pk=post_id)
    except post.DoesNotExist:
        raise Http404("POST ENOUGH FOUND ERROR")
    # items = next((item for item in appName if item['id'] == int(post_id)), "None")
    return render(request, 'detail.html', {'posts': items})

