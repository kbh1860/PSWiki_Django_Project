from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import render, redirect
# Create your views here.
def  main(request):
    return render(request, 'main.html')

def index(request):
    return render(request,'login.html')

def FirstAlgo(request):
    return render(request,'TwoDepartOfAlgo.html')

def AlgoWiki(requst):
    return render(requst, 'AlgoWiki.html')

def SecondAlgo(requst):
    return render(requst,'BackTracking.html')

def ThirdAlgo(requst):
    return render(requst, 'SegmauntTree.html')

def LastAlgo(requst):
    return render(requst, 'ThreeDepartmentOfAlgo.html')

def LoginAlgoWiki(request):
    return render(request, 'AlgoWiki.html')

