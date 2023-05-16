from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,"home.html")

def quiz(request,pk):
    return render(request,"quiz.html")