from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
# Create your views here.
def index(request):
    return HttpResponse("go --> /santhu")
def birthday(request):
    now=dt.datetime.now()
    return render(request,"birthday/index.html",{
        'birthday' : now.month==3 and now.day==16
    })
    