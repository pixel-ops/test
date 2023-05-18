from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.views import View
from django.contrib.auth import login

# Create your views here.


def home(request):
    return render(request,"home.html")

def quiz(request,pk):
    return render(request,"quiz.html")

class LoginView(View):
    template_name = "login.html"
    def post(self,request):
        return redirect('home')
    
    def get(self,request):
        return render(request,'login.html')