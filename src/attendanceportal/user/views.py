from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from .models import User,attendance_pool,subject
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
  

class Base_view(View):
    def get(self,request):
        template_name = 'welcome.html'
        return render(request,template_name)

