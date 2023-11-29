from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from .models import User
# Create your views here.


class UserLogin(LoginView):
    success_url = reverse_lazy("welcome")

class welcome(View):
    def get(self, request, *args, **kwargs):
        user_role = request.user.role
        if(user_role == "Student"):
            return redirect('student')
        else:
            return redirect('staffs')

class student(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.userid
        template_name = "student.html"
        return render(request,template_name, {"user_id":user_id})


class staffs(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.userid
        template_name = "staffs.html"
        return render(request,template_name, {"user_id":user_id})
    

class Base_view(View):
    def get(self,request):
        template_name = 'base.html'
        return render(request,template_name)