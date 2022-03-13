from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def hair(request):
    return render(request,'hairloss.html')

def weight(request):
    return render(request,'weight.html')

def skin(request):
    return render(request,'skin.html')

def nutrition(request):
    return render(request,'nutrition.html')
def depression(request):
    return render(request,'depression.html')
def sleepdisorders(request):
    return render(request,'sleepdisorders.html')
def weightmanagement(request):
    return render(request,'weightmanagement.html')
def workholic(request):
    return render(request,'workholic.html')


