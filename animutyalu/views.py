from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
# Create your views here.
def index(request):
    return HttpResponse("go --> /santhu")
def ani(request):
    now=dt.datetime.now()
    month=now.month
    day=now.day
    return render(request,"animutyalu/index.html",{
        'jeji':month==1 and day==12,
        'ujju':month==2 and day==6,
        'suhi':month==2 and day==10,
        'rusk':month==2 and day==17,
        'santhu':month==3 and day==16,
        'tom':month==4 and day==8,
        'suke':month==4 and day==20,
        'tharun':month==5 and day==20,
        'gayatri':month==6 and day==8,
        'moti':month==6 and day==12,
        'jyo':month==8 and day==28,
        'akki':month==9 and day==6,
        'butterfly':month==9 and day==8,
        'puji':month==9 and day==10
    })