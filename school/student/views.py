from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    print("View is called")
    return HttpResponse("The home view is called")

def my_exception(request):
    print("View is called")
    a = 1/0
    return HttpResponse("The Exception page")