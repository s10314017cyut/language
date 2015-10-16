from django.shortcuts import render
import datetime

def main(requst):
    now=datetime.datetime.now()
    context={'message':'Django is very great.','now':now}
    return render(requst,'main/main.html',context)