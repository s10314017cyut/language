from django.shortcuts import render
import datetime


def wiki(request):
    now=datetime.datetime.now()
    context={'message':'Wiki is very great.','now':now}
    return render(request,'wiki/wiki.html',context)


def about(request):
    return render(request,'wiki/about.html')
