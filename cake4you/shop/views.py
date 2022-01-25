import re
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
    
def basic(request):
    return render(request,'basic.html')    
    
def tmp(request):
    return render(request,'tmp.html')    