# -*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import datetime
from blog.models import Post,Gallery

# Create your views here.

from django.http import HttpResponse

def hello_blog(request):
    return render(request,'hello_world.html',{
        'current_time':str(datetime.now())
    })

def home(request):
    post_list=Post.objects.all()
    return render(request,"home.html",{
        "post_list":post_list,
    })

def index(request):
    post_list = Post.objects.all()
    return render(request, "index.html")

def test(request):
    gallery=Gallery.objects.all()
    return render(request,'test.html',{
        "gallery":gallery,
    })